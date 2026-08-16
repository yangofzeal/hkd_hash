# HKD∞ OBFUSCATE v2 — STATIC PROTECTED MODULE
# CPython 3.4; all protection work occurs at import, never per function call.
import hashlib as _hh
import marshal as _hm
import zlib as _hz

_B=(bytes.fromhex('066a4bd33f26d6fdf9898f690b4f94205396f88fedb7fbd7259fdcfe0f1deacfb705c536db9427756eaff31325b221af7d8dc2e0afa36dce772a31ad7a87d7b77ee6f992bd7a4da52484f8b5276ae717d89b13f8bbbfc419a122bd9c0b7a66363aa5af72006e8d7adf649fd450964aa6631833ab707e16da3dea146d79c13d16'),
bytes.fromhex('7456d9ee5c66780951781039d82216dfad8ca065a5c9d42f124ad1bc3c056745bea2cbc9'),
bytes.fromhex('0c151e15a6f2e45fbc390ad88bad93197bce78223c48d1542b58f813900dc7766089a32e7538c346307b832d1c7cc854f4b060ba7caa1c4017f1bc03c6e5922db4c11549f8927172fdbd2fbc5f29316551d4f765d3d860cac00239e1a6661010d3b27c74c1d0076a1a64fcbfa4dc84da3cc0b4c8801852d8a780b5cbe4c7e969'),
bytes.fromhex('aa727568e0ab18b67be35c5799aef55f2cd6d1d128807a4dfff449381de35043b0b1ae2f11467b5102d9375a74c00b2fd1ba18747cfceb6842678faf40d3c9b922471bacffd3623e0c301baa2cb1a264020b556724a76e0339806587419a595d0500037c532973377148c51328ea4898c2169803a37b69b472c65f9a9180d189'),
bytes.fromhex('af7b365853a1c4bea0dd89a11137e67682754216a9cbc8581e3c5b00bde3ba0b98b3958a42678781c65126e56bb432f0651087f72978f6102b3742c4d911ad500e2220ca017b05a67a8367f6f40f8fba223163a795522f5f0a0ee03f087bb1c231e2ea3b897d0a80d2d5beb59f6956066b6b940d5f510ee94c5cc49476db51c8'),
bytes.fromhex('9dc4edc8d8132c80a82a3a8772188083eea3adcd366befc73f8ee7717f9f578ad68d341fad57323f64f5df7bbb7d913a8247a3ee6cb0cc7a14f94f4da559a30470bf98a75bf6d33b33e1326756307276f1369f107b339145f99ddab1ab211821e62d4232c575a6a29ce8cc9094eeea79a9b8106718ad13c1e45111a47931f8a4'),
bytes.fromhex('bec518c320490753af4da3b780a17419e41d4d5f51a901df69cdbf605d3b350721c1c93daf2ea4ecbfc3731d66b190e03ccf20f193e260eae2455100f41bc9a36975320fe27c129acdab10e212cb2180af681e94eae3c30284025a519175a89efcd7b90f3abf70e214de43fe5c31af753747facec4f861d6a0edb5b351b5dc21'),
bytes.fromhex('90671fc87067087feb884816386bd6df3828db31f28d5c60858212b6f7306166fc3e81ff2293ecd1c8fd40614db5228c9ce90e05fc302ec5917d4fd70e341b2c5a8abc8967d1d4ff8f51e6bacb4a7245845e64619037ae3a06db1e326e0e0961cb2900aa320ff07ee551344489b5dd989339e34423c51230d8c587a4686fc67a'),
bytes.fromhex('b18e1367d45761fc7fda45240c596a678529d939a290a29206b4591be908bb68a5aa87a7335de9b48adbda13350717600c845388f0f32af7c58939c024bb04233ed317c4f47e2c323b044fec09a68bfb5cc265620c6f5e44be7e4122d570566375244f245136e24e5a72b0a63c1a62a4ca6a5fadbd64d319481dfc90020a2df8'),
bytes.fromhex('ecc530c37201ad0a9625e8ca8f267d0f2e47a08c13ed74bc2e37289fe4270e85f98d85df7ee37448e75b2346f77e72336f496911a8fb9a3cfb098dc857def11d834bff9b2a20cd2ae6399a57179c4b4fac4961f28c0787199a216f111437f47710abd1f6fe6267b7621d1a8ddbd44dcfd387eff50874b7793a534e2e5d399557'),)
_I=(3, 0, 9, 6, 4, 2, 5, 7, 8, 1)
_L=(bytes.fromhex('72dd004986c5cf6cceaac8cc203bf53c11940fdba442367d6a71844e35f1d428'),
bytes.fromhex('4dfe751f8beba0cddd84a24987aff1d6a49e43d41680253088e957e761508f21'),
bytes.fromhex('3dae722972bba1704157f48062460422aa1a1a469fcf8587f58c868869943933'),
bytes.fromhex('aec860baba362bc73683d9ef4a5f46a1fd6990ff80a222566f4669837355427f'),
bytes.fromhex('e2d510645f8d0041fd83c9106c7f04a2981139fb75aa75a81a8f7bc79b98e86f'),
bytes.fromhex('9cf30f224e595a2e99ffaf64d7e19696f89f800a2f49ba84f40d3638bc720ea6'),
bytes.fromhex('fac4dce64bee334690eee00da0fe2591ab9ac65b3c2b29ee461c124bbc879de1'),
bytes.fromhex('5dc15e3ddaea1e8e9672779d0a7f8cbceb8a489fa3fe3b9969fb05996a2a5096'),
bytes.fromhex('17557685566a1d5fe14c7cc611b5c93e33e0cd71d2316e93748b49b93f99c8e8'),
bytes.fromhex('6100f4f8c8bdf0736b49b32c19718ef4aed0db16b97785f7856025dd35754041'),)
_R=bytes.fromhex('de4998b8f4681f76987e35391be638c876d84ddd23094adbcdfa49f29890dd9e')
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
