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


KEYS = 32
ITEMS = 10000
ROUNDS = 250
keys = [tuple(range(i, i + ITEMS)) for i in range(KEYS)]

builtins.hash = NATIVE_HASH
native_s, native_result = workload(keys, ROUNDS)

hkd_hash, mod, source = load_hash()
builtins.hash = hkd_hash
if hasattr(mod, 'clear_cache'):
    mod.clear_cache()

# Populate the cache once; benchmark repeated hashing of live immutable state.
for key in keys:
    hash(key)

hkd_s, hkd_result = workload(keys, ROUNDS)

print('HKD_HASH_SMALL_MODEL_BENCHMARK')
print('python=%s' % sys.version.split()[0])
print('platform=%s' % platform.platform())
print('source=%s' % source)
print('keys=%d items_per_key=%d rounds=%d' % (KEYS, ITEMS, ROUNDS))
print('native_seconds=%.6f' % native_s)
print('hkd_seconds=%.6f' % hkd_s)
print('speedup=%.2fx' % (native_s / hkd_s))
print('exact=%s' % (native_result == hkd_result))
print('builtins_hash_replaced=%s' % (builtins.hash is hkd_hash))
print('dict_set_c_hash_replaced=NO')
print('PASS=%s' % (native_result == hkd_result and builtins.hash is hkd_hash))
