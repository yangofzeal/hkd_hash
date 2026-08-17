# HKD∞ OBFUSCATE v2 — STATIC PROTECTED MODULE
# CPython 3.9; all protection work occurs at import, never per function call.
import hashlib as _hh
import marshal as _hm
import zlib as _hz

_B=(bytes.fromhex('ce408b8347a9cab391c88c2c1af0e8fbc59df148c5ae7fd1a71fc1e72667fb198696c9b4c3424c994f6af6a1ca9a127ac2511174437eebe2e302d564d4bb88fc0a886402946f2276f72fc0a3d3352286d56a55e7a2b6ca68cd295105443c2a98e676005ff89776a3ea9184dff4f8697129eb943a0a65c0ce8b4a5523e4928620'),
bytes.fromhex('2029f6095c03876c22b75c1ca3555bb5f2ef5ad14772e4aeb7b2f7112ea003670e00fdac95cf7f3c40520038efec844d61f94c23551f97005544c6e2637f7bde7a60ca5e93d941ce87d78ffeaff7e8d46256385729da42f983cd9e2ecc5789f58ff22ca17f8a7616eed3b2a104786f027ac331fdab3f35b5e64e05da2d8f9cf1'),
bytes.fromhex('aa727568768a1fb47fd35b93bfd4596ab8997cd95a58f95e150bb9bffe349b61bae4a5106c5e436b8eb04e86ff2ed582dd549c5a511205ad943b9860b1ecdfb34d150ea04e2517d39517d06b1794ca009fc90bf23830d9a6f4a5f95315a32e4e71e2c56d4bd761db3ca940696f8a37dfeca6902b5a1676a27f0fad2b0dc0a058'),
bytes.fromhex('45a5dc9f3655850fc0e1efdf28c0eff51cdcabb570fd7ecea56947c1c29fa9459a13d0b72fcd75b711df8b2f6ec989ef979bcbc38226b1785265ba7be18c57e5437dbff27255b933a1e034a27ffb68a68f9ec097aeb72c292b3318458d5c73fd39e92dce656fd9a55166af2acb6862427eb902b7e1440e2ab873781dfe702d41'),
bytes.fromhex('7838da8a7b052cd1fecea1bfc006e6272af8b37aa63a389b83fba06b00dcd20c7198bd927e7b4b986e26056b1974db43d6c6373630317347c415710f1f951b5a143a61c06a3dfa27037ec0f8dfe2a1b0f4a19a2c13127384483eb522ecfc5e98e84e090d3c87149659eb1e17605efb057d3c50a5620a62619c9041ef720e1b5c'),
bytes.fromhex('5c3e66c76e4ba7acb3bfaba4c4c215508ca9e8c76ce7b3c2078d895d930917fbd65f4f6ddecf9571775ad64d55bd47ee357f5c956c6fcb4a29687d2661769c71adf3652a2a32131393fb267b785e947acf7382196df8d59688f3953d5962bb6e24d0ffd224ee7b633a52f8c9f7a4bbe33a44628e6a4b55271d91e127fd67b0e8'),
bytes.fromhex('215d44abb4ef1673f3250ba4eb0bc7f0c44342aa0500d1e0ba8c445a1fc38fef8759687d9f207fdb9fb9504fd7031dfa16c2f8ae9ef75d7cf67c538aec00d4639f17e3ea3002b4f8dd9ad8c9e1a2b2e22a47571e06c596b28a3b59da61d69ffb0daca068c0430e67ad9ba66fda4fbec8c50d6e36831bfe5527ec6eeb1bd22ab1'),
bytes.fromhex('13b87fc428618536a6ce8dc7b1482e4ce30124d9167931e64949658f1a4048a920bdc26b38e35b6dd144e743e38a68902e81bab8d07ed539ae2decb463bece69a6f1364ba83b4ef6a22bdaf92f1c95a5ab7b74aa0a0b019d8b11aa9075d79c4e000d96e500f6c3e879fd84b0fafbcdc64e8b08f480902f5f19b8c65c7774771d'),
bytes.fromhex('f48c7062ce52ba94a4f541c5b3ad2769f62ee6715a00f55a3d72673c7e6ba6e68244119cef1d08f30bd1d75e40891147f58315d075b2f9b0529f1c13edc204b22eff8d0f2d649076dc264d51d456f47080051df819463e97bc1ff1ea8633ecec7e0ed31c764449eaf3f8011c66bdd94e49c4c5d84ac2c927'),)
_I=(2, 5, 1, 3, 7, 4, 0, 6, 8)
_L=(bytes.fromhex('428e5b00e72889f3f52ee26ce6a1ee36e72f13175f445cca2509d342cf61c365'),
bytes.fromhex('5823ff7f6ced827521f61c026d40f5466df97a760c0fbfd5334bb8cae2dc4df7'),
bytes.fromhex('22cc0b5f941cf01399a842bb1272cbbebc08c503d88ebcb4c07b4ab9f4d4e980'),
bytes.fromhex('11a4bc167771b3333f3b5d6426300067f08d281e30ad89e72e24ae5fc6f8d198'),
bytes.fromhex('3d6e5e0be0a68397e49e73973239a8579a7961f864902fa34408c074c169f0f6'),
bytes.fromhex('250c0d9413eb9396c882f7bbc03a9cc7a96b86d7f7785e76d4e493e94e0d14f0'),
bytes.fromhex('666106b92241dc4f13b926e80ef06eae521750ceb45f7c26afba33eac652052c'),
bytes.fromhex('e5622730713374452725ffdcbb15fcecb75f70e19ab59f156cd2d9425971fe1a'),
bytes.fromhex('b75c6c3115f27bfb0e658c3bfc6459af2405cc16f6511073c2f78a406bc30248'),)
_R=bytes.fromhex('ed96c59f7083d40433961f6e58a4c7bcd94182966afd2a4d8d4ecf802093ebdd')
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
