# HKD Hash

# Up to 90×+ faster repeated Python hashing — exact results, drop-in acceleration.

HKD Hash accelerates repeated hashing of large immutable Python state by caching exact tuple hashes instead of recomputing them element-by-element on every call.
```text
from hkd_hash import hash
import builtins

builtins.hash = hash
```
No application algorithm changes. No @jit decorators. No approximate hashes.

Same Python hash. Less repeated work.

Benchmark: large immutable-state workloads show 90×+ acceleration, with exact hash equality preserved.

Free vs Unlimited

HKD Hash Free accelerates models up to 10 MiB.

For larger workloads, upgrade to HKD Hash Unlimited:
https://buy.stripe.com/bJe14gcX17sb4boaR1gUM08
