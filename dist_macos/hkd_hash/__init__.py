# HKD∞ OBFUSCATE v2 — STATIC PROTECTED MODULE
# CPython 3.9; all protection work occurs at import, never per function call.
import hashlib as _hh
import marshal as _hm
import zlib as _hz

_B=(bytes.fromhex('98cf628fe7176f77b4b5563fb8efa2961e9ecb96605c0fff049977bbab9b34b8a11b2f58bc2822faec2e558913000038a9a8495ab11545b45ce68be6425dd006ca96b8a6a8cd7ff72170e93ae2506ce35e378b3fceccf06fb0f96bf45f5212c6283d1ddd8b4121ab786f3113743857088de31a804224da408bfb0c072e0bde79'),
bytes.fromhex('59968143043bacaa0ad96b20708d533c5b5b7758777ac156e1526eb9bbb58e8d833dd22279f7f941a0ab91e543204d404001a94dda447654674842f1c281675e16e9d60e54db6b9aaa273915ea364ae6def07071dd86cb6009bb584c5c06e644d5afe76fdced43f86094ab2d7fb88248a7151dc6c969ff015d9504c4fafa0936'),
bytes.fromhex('fca1b7af7eb793eb2c4585559d2db285208b3ec04279017aecf3ef8ca8074145bb2a5d9227a42e42b9649f91eb67f3e5edaf235744ea174fee1af94704cf9dfbbf2081e37fb65496588fb63043c79fed0232d28769e657a88be4471180d964187d9a3e07dca0cdb04e2ac989dfb98a412552a9457ff37b797210bbd3f0569cba'),
bytes.fromhex('62a527bcde103b5b86e15c2b594789a730ad8fb85289e1c6948a4fa1f29d513727bf1b35f9c89804439898ce37b1c16411938dd9964bfff33dcf7a418f70d9add4caf2'),
bytes.fromhex('541cdcc2edf32f7d4915e5e1afe16f33bc7a280d2dfc9ed854d8a6b4931724fdb67582e3b1152b8e19536c7e609a7d8a904a7d6da93e1d224f2f3ac18bd6825ad64da4e6e90991b473c4ece472ed9bb27ec5f060ce7b916028162826bfbe219722172c6a590349791d7b9490cf81960b83e5400b2519d036f0d494abd05ba18d'),
bytes.fromhex('cad9b765b2d40dca3672b25436892de7692bb16245bcd364c1eeddc9c6b6e84c16d44dcbb1ad434fe4fd507e0cea8f42248185d235949ee388e7f7d8814c28214cc9d063a70540c849786c907bcbae81fd3f1fe50b69f76eeb57f53f5e1489375e86a760a064db00b30ca87a5bf8b90e142c56d675a8080335cc7845f33d91f4'),
bytes.fromhex('1653da5f2091dcb494133ceabc29326c97da7e9220436f4d8be9a6e7b021016dc45dc4b5a098f9f04e9363ed35c110a09d91b3a3814f7cf75b0aaaed835ed02f008546eaa019471aa85ad6f9b4ad39f482560ca1b9cec971fc7c1ffd69b170c0e0fa8b18d5c7d392060958d3cf4a2fbe82a1234ed73e91e194f39c5ddafd0ebe'),
bytes.fromhex('aa727568628a1fb47fd25bd3bfd459ea81f6f89f4a524c01d81682dd5035d34a6d0d5f8d015cfb0e0376fa5ae33bf2348799af6fe44d29bc52d75fe4b05e31b112acfbc0c0684e582b87a536fa788382894b625d973a371ffd8473a3f4dfecf463e674517701adebdc7b4bc7eb9d6c3240260a1262e5513e6fed8b9a41614562'),
bytes.fromhex('9d36ba94d24d29f6b9c5958ddc9e5e43ed0d55c4e0b3854aa13a04824756f152eadd047181ead6513e02e086fb5e64087508b08d34b8915853044c98b204ac8cfb69e88f49c1ccbd3a3ab111035647364433fc50723d2282f0923bf2dbf2ee7b5d584620ac5be6ec032e5fbbaa70427b4024c2d830762fcd02f1f4500be4a774'),)
_I=(7, 5, 4, 0, 2, 1, 8, 6, 3)
_L=(bytes.fromhex('ca54adc0e323fad3beb508cf214d8e047cc011e692e339878065e8e4c31bc822'),
bytes.fromhex('9903fa9cf245229bceea6759a2f0975c6bd94e3c2ead67d33e1ebe11064be400'),
bytes.fromhex('a0ea2f010855b4c6c5969dd8e8d9183a9421313b0f0819d7c751ce49452253bf'),
bytes.fromhex('785938e53d74391c13b51645cea8b084735b5dbc3be7b486300a3d34c85ad832'),
bytes.fromhex('fa79ae5e2885e521f8096599f0576fb303bedc4895b5f1f5922df329c3622913'),
bytes.fromhex('0051084fb8bf96f9d4779a9beba876a1c7ea74cb3aa84d868c249da93d5e78b5'),
bytes.fromhex('0c3c093858e07c5b608b0a32a3ad4b43f9980230e41c28357b5feb6325e5c53e'),
bytes.fromhex('894266f857a9fb66da1677808c4b11e990378757af4586922a3e999e0a284e10'),
bytes.fromhex('73303e599a520a9778e4b5c8b1962dc0abce3eb52e9c7c3e891d3d70aee3679c'),)
_R=bytes.fromhex('5aac002851e049fe0d3eb4579591065930e239b6bb28324d1b10c5eab4758a1b')
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
