# HKD∞ OBFUSCATE v3 — PYTHON-3.4-COMPATIBLE PROTECTED MODULE
# Source payload; no marshal/code-object version dependency.
# All protection work occurs once at import; protected calls have no wrapper.
import hashlib as _hh
import zlib as _hz

_B=(bytes.fromhex('bdd98a91fc4f91887a4ad55c808c4a58309813966f3355165cd967922f516ac7bc660a482ccac96b3b16a6d5eab65061a8a423f4c46fee37f38f4d36a14fc91045200ceceadbc2ce9125b8a9d6ab843408fb45ad5949a5c3707022b14ee57135da1bcd047337edda2fa05f05e0d7d58e36e7df671759370244e0860addedc29b'),
bytes.fromhex('d95d07de8dfca9f2d188163f3c3ca0fa90a1'),
bytes.fromhex('aa726568cc8bdfc77bb30d69dce68a87687ae07a0b3941dc0d09bada7868c8980107b311dd3f3352d62edccdbb037849112d90a464b77ff9dbe1b1343baee5019e583cd022773640151a6e280c4cc7975dbe99fa7ed50d8eaf630ca47077927951f41d394d941939ed7a91d1cba85db485049cce25163eef1916a9236314a31a'),
bytes.fromhex('d0c776cf71b4ba7c12600f15dd1b8ed677c807156f048d1ea4ed0232c233c3a605a9823a60b3f891f89d09de115ef100dc8c1e70040089cf3cd33d856ad4408cafa7a56805836ae3e2f345605b6ffb899d66de8bf49f773aaee3a2bcc9fb4d85a972eac2cc08d54a309de7ed2a53ac73538fe581ef66cb6fa5387ce83fa6de53'),
bytes.fromhex('526c4256130cb6431db8abd1ab0e7fe5a29dcf753b16259c77d2355549674f6dc3d73f9c280fc819d27589821b3e8863f7ebd5028b80b6e57f8f66a930663ea2cc15adfcbd4b426fd9b31ed3f0eb0ec549cabd66fb2f013610f9b9ab35f8b236c4b4bcd62143b55309b1f2a1d0dd460b617f9667a142c51357b97d54cb86658c'),
bytes.fromhex('746e81446ea5a83a05111fbb957d05ecbd3cac68ac6a9baef6c70430237f118404e5b70e742e5e724addb1f315583b0eae4ff472c11dcb1e759eab4a1d8203a482daaefac196849c95a4736dde4ed25b9108f717951037bfa6beac4a20d51beabebac506fdea5e91c51994d3fe465a9db39d250fe2456b88ba5ae3e8dce7966c'),
bytes.fromhex('18b6769f1260b4640a88525c6ceb3452690f4fc2e318695639d718fc18a23965e6578fe75020abc00948b641759955c900cd25bb4b5d75e716985e347aed9bc3c06ee697e2340cd48f7093b063485a61d65b59796d2baa6a33dc26c2f017b80d5cdce336e23fbde7576c793bb5404bd49a2b047cf34fe866e4226cfca376547c'),)
_I=(2, 4, 6, 3, 5, 0, 1)
_L=(bytes.fromhex('b0ddcddf4de95a09f3c8d17225c2f32d32bd38353675d12524eb14501240c6fe'),
bytes.fromhex('0d72ad0b2924ee1423e8dc6248f6499be545b2d00b65ae3df5d8b6b375a8bd89'),
bytes.fromhex('d6dfeb1b08f8de6791ebd116b73bb7c38dccfc0495949a452ebecb9bcb2f7ee5'),
bytes.fromhex('ecf989ba759e7c02ead89dcc35563e9f6670f891d90b9ed034cb260dc5f9b7bc'),
bytes.fromhex('ce272240e54bd37c73319faa3183891bb87639990582dc4678d8e2aba0297aa4'),
bytes.fromhex('858cc6aa35cf49774a773d2aca1dd1f0ccca985b47390f0a0ab736d827469a2d'),
bytes.fromhex('21a8df4a0d0c4e6360bbc616838af469567f793bedc09433404a82568bb037a7'),)
_R=bytes.fromhex('2ddc43620242b4bb6c8353fc32412665ad2d4790fe17e52c598d6906e693dc11')
_S1=bytes.fromhex('b4c44a1d49f84630e6a3d8f9e940b5fe9bac91bad310595a9d955dd8b13e68ff')
_S2=bytes.fromhex('7e50262985a1f8adbb970e2cb7aaab9a1c50293fd48e23303c28fc9662bd3098')

def _x(a,b):
    return bytes(i^j for i,j in zip(a,b))

def _n4(n):
    return n.to_bytes(4,'big')

def _ks(k,idx,n):
    o=bytearray(); c=0; s=k+_n4(idx)
    while len(o)<n:
        o.extend(_hh.sha256(s+_n4(c)).digest()); c+=1
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
    _V.append(_hh.sha256(_n4(_i)+_r).digest())
if tuple(_V)!=_L or _mr(_V)!=_R:
    raise ImportError('HKD∞ SHA-256 integrity verification failed')

try:
    _S=_hz.decompress(b''.join(_P)).decode('utf-8')
except (ValueError, UnicodeDecodeError, _hz.error):
    raise ImportError('HKD∞ protected payload reconstruction failed')

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
_C=compile(_S,_G.get('__file__') or '<HKD-obfuscated>','exec',0,True,0)
exec(_C,_N,_N)

for _q,_v in list(_N.items()):
    if _q != '__builtins__':
        _G[_q]=_v

# Functions retain _N as their normal globals dictionary. Remove loader-only names
# from the actual module namespace without mutating _N after source execution.
del _B,_I,_L,_R,_S1,_S2,_K,_P,_V,_S,_C,_i,_m,_r,_x,_n4,_ks,_mr,_q,_v,_N,_G,_hh,_hz
