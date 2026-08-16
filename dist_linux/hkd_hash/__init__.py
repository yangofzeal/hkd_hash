# HKD∞ OBFUSCATE v2 — STATIC PROTECTED MODULE
# CPython 3.4; all protection work occurs at import, never per function call.
import hashlib as _hh
import marshal as _hm
import zlib as _hz

_B=(bytes.fromhex('aa727568e0ab18b67be35c5799aef52728d6d1d128407b2dfff449f8c383e1569377799ab959151fa82ea0437310c844a94497beb512ab9d55aaf9954cd094c565ca60e3bdf48689e39e1243a2b06a387ba92e3404026af36d9134c341ca5c29db849e102098c6b45a7ac33fedd4c49688090e0c46fa2b2cc55bbe51f6a2be9d'),
bytes.fromhex('cbfca914ed66513887688156a78de7b838a035097ba371e49fc7b2b438f22d5417311d7256356fb74add18e46ac13c5c06531687a83f1471e17ac29589986aeed245888e555718ef8bf444be2bd79d8c3405ce009143b61c55f73304ad47026d244c06b0de001f64d6dd87d58bd3e38808bec446a2f51f4defe41d8cb5ca6c49'),
bytes.fromhex('f257fac48030bea06c2f7d8c0d4b187e89b8b1814e4840b0b14af3df234956eabe06dee35a85c1603fdd0f35ce29e85a7757c5688f9c8086174af65b6fc1e3508acbc3e53d1d65a3ec1c4d3962964cd7d14c77d51ac730eba39f6a36e4070b880f2a7ef7b2fa8ebfdf78b794ea8d5b88ab111e4647fc19db71a2710050d46be3'),
bytes.fromhex('39a3a75a7df49b1fcdba76ed02d43a0f74773b789cce8fcfdbf799056ac23653ddaf2712816e6a5daaa0f7bb57287b88a47b517777c805d72b0573d12730f954851627c20464c9349d2398b60510a93122fc1f62f1d0ba5bf1ca44962c97290ae21b800166acdcdcd5dbdc9cb1b52fe0581c3da0d04f934e589509f1936d852a'),
bytes.fromhex('7ed3fc413686e7391a1339032ca45ce66b692e85fa1afae71f97af9059fb274903c018ef1bc585861fe8ed07bb3109730b513d7f2efb1dd3f452c97b8efe641a71682f68c79bf96be76f32933770865458e49c22d2dd97f4557d3dbc83ef497f961c9116568033b97799ec7830a4fabc857ddea805c5473ad064917d8c89fcd7'),
bytes.fromhex('5d6790cec573b4a2bddb5de56f14a154f38e0e23'),
bytes.fromhex('df10c22ee7ee64a925685b640d7388594fa9819599cbe776d48d8f7004f8cdbb891afa7dbf83263bfc7548206ca13c0797a4162b0134042aa552229455fc9dd79b95874208c7e755b41e3f859a15bb24de64d7a83f164cbfa1edf9f54a10fc7e4254a2d6399ac0b3f98d66cf79ed5ac7a5c0591034f56db893aacafbd8489bb1'),
bytes.fromhex('c7ede44e5a4eddcd5ecb077db4bb381f96f61121a54823e7136e3a06c3d2362a61a82e911275cf9a419c62aff323d1d7340c12ebd852dd5a5f5d8d77c385bf4ed7bfb4670e7b2a0b6fa4fda026d59af37408d119e07e00b56c0e371b16760f7f72412b9c0390215830b56c283e243a11c3059394c17eaad4545a30c669ce84dc'),
bytes.fromhex('dd7c90d7587c27ee2782f23aecd4ea4cff4064e21dfe6ecc2a07761b977bed957c965b9746dc7ff41480fe481eb3fe4333b7e1bd41514184adabc4ee6b638eb620ae32d6fe30cf195f0308137259d946572cc75958853bc6e3b39a08215fda2daa105dabe547699f08b9428b742a20d97df561631a71c89bee9bc192dc846ed4'),
bytes.fromhex('1da4cf39309aadd791ae19ca4c04637e810c26db8a2865f8e69a07d48dcb4ab98c358d892fb53a55c4649102b237a53ca4394c186e2b97202858ce9317d72e06227a33009ae2bb7e9dd280a983460ca04ba4640cf675c2c6640df4d385127774bdacebebb0f284e547467714af98b195dae4d91a62a09e45551daa14ab5f8cea'),)
_I=(0, 6, 4, 7, 9, 1, 8, 3, 2, 5)
_L=(bytes.fromhex('948381c2e0ebae13cd8fe3e69adc9f75e29377c3eedff0152af080201efebcad'),
bytes.fromhex('264525ab47eb6ca2670dec1b637c2f03dbd5c82f764ba31d686a3012fd839c9c'),
bytes.fromhex('29f96c96ed4f68793def89c61035e125060a7e7c8ba70e08a27f6215d3388f69'),
bytes.fromhex('e673721be8a125f32332232a76bc2f5197545d8b0191ba709b778f2387a093bb'),
bytes.fromhex('899efd4afc881bf1c7703239cf1c362604bf0c24e2abe6fd223d35a386b3b74c'),
bytes.fromhex('f1740bd5711becc03df409b57076ecb50adda3cb743958f7905147cc3e9034ae'),
bytes.fromhex('651e30a3a5d03ffd0b196176583088af0dd4b84f46ced985a1f6168c059ea007'),
bytes.fromhex('e1278d2734ec8f322144f9e5d1e876012ab42fd3006c5e97bb7dccae2271ba0c'),
bytes.fromhex('683386eb426b94d50c4c67050963cd48e97cff2b8698d2f4a3dce73259240f57'),
bytes.fromhex('d4af46f8b26c5ed2b3f65c15b32c996132f8cd2df8f53453a8cf772865486659'),)
_R=bytes.fromhex('c10145971c6b0958dc043c6e17171d85e843d41cd6883472bb23b274a4d73e20')
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
