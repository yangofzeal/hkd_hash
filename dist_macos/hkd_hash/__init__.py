# HKD∞ OBFUSCATE v2 — STATIC PROTECTED MODULE
# CPython 3.9; all protection work occurs at import, never per function call.
import hashlib as _hh
import marshal as _hm
import zlib as _hz

_B=(bytes.fromhex('181e561cc4ca1dc80f52ba56268faff82bff3d8efd9ee487f3a1adb95a5ff80878f613288fe3eb47ab1ce866cb2b847f46c2fd5a94e68664a96d7d3061755c71adf0152a2a32139392eb327b785e947a37152c58d635c52b35c0a57d5d45e414e53e991a99ee7b63ba52f8c9f7a4bb633a44668e6a4b55271d91e107fd67b0e8'),
bytes.fromhex('0d591e00c164538d50c2baf9e0fb4bf8f62cf5c2040f4158f96570baf96ea9b76ba77b5de6e26d08039773735b61ddee6b74b1a97ee51eb6fac5e4ab12255a0a0395ae429f0e7876d06251dc8df4f540a39716c418c05404374d8d171e26f00c50ba65092f73d009a930730cff6243210aca81f9c2a1e9712daef2c3b79e52f9'),
bytes.fromhex('87c23a14c652ca24b05639d458e848398288656861229dbe00d365fb5b390bc7ba83bdc8963dd81145f255aec7031ca784021208f84d9e4f7aafd498313ed1bc29aed584a13f825879596a6fc52985ca2068cca29c04afe1f4b1673cd8ecfd78b076b6f4705e6c7127cb4efdbe1b28273279653531de336f0a46f398a46afd05'),
bytes.fromhex('aa727568768a1fb47fd35b93bfd459ea81f6f89f4a52d83e6c6a09347e75d125c2face3df147a3559aa78d4da7d0033602fc34e4efffafc30051087ab720e560833ba0a132942554d5151109f823e2078d88c07fd76fb2555c5251c4132fd0d37e390a034c11fb4fd894d337c948c2c1f846a52ace198021134e4750eb9722a1'),
bytes.fromhex('0029f609540b876cd2aebcfa5355db142af75718e850efe13fccf2d7fcf821790e00dd2c92cf7f3cad8e95b9a70f493dcef1af608d22feaf63e639461a8c122d0d21350da67724f9944f4ef8606639b7534d07c2e998e84362530ec897cd1b23e0ad0729a5fccae556f3717e68c415b6df6bfeaf2b3e35b5e64e05da2d8f9cf1'),
bytes.fromhex('5975a452d241b3537907ab45bb6d3e1d1489e727078e5cc442eb5fc7344c111e60b2e8a97c4a07675582979b436c8fcf64382eacf1245a678fedfee026b9b5c29bda9e011d3fe8b432091427977a9cf7895c3f143350785973f8a96022909fcc2ef59ba141d9acd66e180a48948cfee444efab952f4f'),
bytes.fromhex('71ef65af1f592e2f1acf03dbc65702af89a7f5efcd334ef062f75d3e03287d24c4b6467eb717bceb5c0e781c4a1e443c6cb5319865a770323cc89fab27511c8e45f113866879a33743fd37ec0e7f38a6a95831fe1f23295406ef8f372676ad07be47d90aee3965f305080d7e2199cb4e0aa19cf8730ed2c73b16a07e01a81b6a'),
bytes.fromhex('310d72de9361092e481641aeb3f3c730ff7c6a81ebb12c62456922b9fa09fa662b4ef3d1d58a6c857d43b22e279c18a70246552961c923c09e63aadc7583f0843ef7746a6aedf5a6361cdb8e1686bc58ce44bf7cc1ab898f5db2d2df93560b2a3ad155ca63422bd52eb9a2b25b3bc26991d02b05d423d20ff416f702aa0ac6e3'),
bytes.fromhex('45a5dc9f3655850f40e14345d51bd8ed1cdcabb518f8c7d711067fc1c29fa9459a13f4e692d89a17c8dde15a13ca7a8d4a4db7497455ac93472e2372a711bbf3cbb862ec5a10a957a9764f9a36fd0ce6204302cc1ee30b8ecd2761b642ae8b3d1d2e541c9b8466c60f75856ab9ea6ff42b465d142d88e66cd18cb24b36f8ad63'),)
_I=(3, 0, 4, 8, 1, 7, 2, 6, 5)
_L=(bytes.fromhex('df2ee2479d05641a0877741c2d4ed9f1bca5fc7fe5d81f4b5124b9dfe67063d3'),
bytes.fromhex('1629e6c4fde71942e08a75c05ba94463bd2ba4642057142ee0bd494e56b16b36'),
bytes.fromhex('82af091483ab99dbb7bb864fa774690ba452139765917873a40cae57e6e12639'),
bytes.fromhex('f77cd8a0e5e33988a6f142b3c3a116b7551a3ad49fbf0361ea4502bca91c5e53'),
bytes.fromhex('cadb62d471781f031f7f30b554381b63ad396ddeefbae6ba789d8a3becb490d1'),
bytes.fromhex('9d09031b96f2ee3640d3a14d355cef86f364ab4825cd1f5750c6746ebf10b1b7'),
bytes.fromhex('a39ab7920e4df019956fe2460a9b6f4eec4130bd4fb90648547a27224c08cf08'),
bytes.fromhex('b58b9faf2e4435dcb28f6206cd4cc9279cd5134118462e7e2a74987226216a0a'),
bytes.fromhex('27dca1b9abf33c7c1ad8c9f28e5c37d5e9de66d239b2e891ea128403d16547dd'),)
_R=bytes.fromhex('cde26ac2ed40bd9093939eece14d8fed4ceba8a4016c35830dfac20afda9255d')
_S1=bytes.fromhex('b4c44a1d49f84630e6a3d8f9e940b5fe9bac91bad310595a9d955dd8b13e68ff')
_S2=bytes.fromhex('7e50262985a1f8adbb970e2cb7aaab9a1c50293fd48e23303c28fc9662bd3098')

def _x(a,b):
    return bytes(i^j for i,j in zip(a,b))

def _ks(k,idx,n):
    o=bytearray(); c=0; s=k+idx.to_bytes(4,'big')
    while len(o)<n:
        o.extend(_hh.sha256(s+c.to_bytes(4,'big')).digest()); c+=1
    return bytes(o[:n])

def _mr(v):
    if not v:
        return _hh.sha256(b'').digest()
    v=list(v)
    while len(v)>1:
        if len(v)&1: v.append(v[-1])
        v=[_hh.sha256(v[i]+v[i+1]).digest() for i in range(0,len(v),2)]
    return v[0]

_K=_x(_S1,_S2)
_P=[]
_V=[]
for _i in range(len(_I)):
    _m=_B[_I[_i]]
    _r=_x(_m,_ks(_K,_i,len(_m)))
    _P.append(_r)
    _V.append(_hh.sha256(_i.to_bytes(4,'big')+_r).digest())
if tuple(_V)!=_L or _mr(_V)!=_R:
    raise ImportError('HKD∞ SHA-256 integrity verification failed')

_C=_hm.loads(_hz.decompress(b''.join(_P)))

# Execute protected code in a fresh module-shaped namespace. This is critical
# for hot paths: loader temporaries never contaminate the function globals
# dictionary with deleted slots/tombstones.
_G=globals()
_N={
    '__name__':_G.get('__name__'),
    '__doc__':_G.get('__doc__'),
    '__package__':_G.get('__package__'),
    '__loader__':_G.get('__loader__'),
    '__spec__':_G.get('__spec__'),
    '__file__':_G.get('__file__'),
    '__cached__':_G.get('__cached__'),
    '__builtins__':_G.get('__builtins__'),
}
exec(_C,_N,_N)

# Publish source-defined names to the actual module object. Functions keep _N
# as __globals__, matching a clean normal module execution environment.
for _q,_v in _N.items():
    if _q != '__builtins__':
        _G[_q]=_v

del _B,_I,_L,_R,_S1,_S2,_K,_P,_V,_C,_i,_m,_r,_x,_ks,_mr,_q,_v,_N,_G,_hh,_hm,_hz
