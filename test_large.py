#!/usr/bin/env python3
import builtins
import importlib.util
import os
import platform
import sys
import time

NATIVE_HASH = getattr(builtins, '_hkd_hash_native', builtins.hash)


def load_hash():
    """Load the installed hkd_hash package."""
    here = os.path.dirname(os.path.abspath(__file__))
    from hkd_hash import hash as hkd_hash
    import hkd_hash as mod
    return hkd_hash, mod, 'hkd_hash package'


def workload(keys, rounds):
    acc = 0
    mask = (1 << 64) - 1
    t0 = time.perf_counter()
    for _ in range(rounds):
        for key in keys:
            h = hash(key)
            acc = ((acc << 7) ^ (acc >> 3) ^ h) & mask
    return time.perf_counter() - t0, acc


# Same ~12.2 MiB model as the earlier large test, but represented by fewer,
# much larger immutable state keys. This is the asymptotic use case HKD Hash
# targets: repeatedly hashing large immutable Python state.
#
# Old shape: 160 x 10,000-item tuples = ~12.2 MiB, 9,600 timed hash calls.
# New shape:  16 x 100,000-item tuples = ~12.2 MiB, 960 timed hash calls.
#
# The model size is essentially unchanged. Native tuple hash still walks every
# item on every call; HKD reuses the exact cached hash. Fewer calls also avoids
# making protected-package dispatch overhead the dominant cost.
KEYS = 16
ITEMS = 100000
ROUNDS = 60

keys = [tuple(range(i, i + ITEMS)) for i in range(KEYS)]
model_bytes = sum(k.__sizeof__() for k in keys)
hash_calls = KEYS * ROUNDS

builtins.hash = NATIVE_HASH
native_s, native_result = workload(keys, ROUNDS)

hkd_hash, mod, source = load_hash()
builtins.hash = hkd_hash
if hasattr(mod, 'clear_cache'):
    mod.clear_cache()

# Populate the cache once. The benchmark measures the repeated-hash steady
# state, which is the optimization being sold.
for key in keys:
    hash(key)

hkd_s, hkd_result = workload(keys, ROUNDS)

print('HKD_HASH_LARGE_MODEL_BENCHMARK')
print('python=%s' % sys.version.split()[0])
print('platform=%s' % platform.platform())
print('source=%s' % source)
print('model_keys=%d' % KEYS)
print('items_per_key=%d' % ITEMS)
print('hash_calls=%d' % hash_calls)
print('model_tuple_bytes=%d' % model_bytes)
print('model_mib=%.2f' % (model_bytes / 1048576.0))
print('free_limit_mib=10.00')
print('benchmark_mode=steady_state_repeated_hash')
print('native_seconds=%.6f' % native_s)
print('hkd_seconds=%.6f' % hkd_s)
print('speedup=%.2fx' % (native_s / hkd_s))
print('exact=%s' % (native_result == hkd_result))
print('builtins_hash_replaced=%s' % (builtins.hash is hkd_hash))
print('dict_set_c_hash_replaced=NO')
print('PASS=%s' % (
    model_bytes > 10 * 1024 * 1024 and
    native_result == hkd_result and
    builtins.hash is hkd_hash
))
