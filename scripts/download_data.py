from pathlib import Path
import gdown
IDS=['1ubUE2GhMiuwesqpjNneVupWaky7bmSY7', '128BcUaeF-KIH8QMaBbG6JpYRFLdcrD_A', '11xjpsbdP8Oi8Vh3EhL9TaCLxD7yLqVC9', '1UTDuo5Qu84GuMOAT7Ttsrdfhj47KLYLD', '1C7yK795D2_RffJGQmku0tOl7aQX5N9R8', '1yNTEbZMWKETbpUaZAeJjb3tPExyk8R_k', '11n0S1Xbro9EOFAYZdhyJWqPBlnxN2d8q', '17G1_VUQkwPQgMBMt72KT0kGLE7rpOg_K', '1OyqYLX1aHLtFaSPfs0gP5_IsVJWoXV4o', '1ecGhiVfH1Qv5PFAExsNTh_Ig5_IbBLOY', '11xfvXksr-n80Y1QEYfHvFRiRCwcmWpGS', '1a6NFu43mESTuqWJ_VmZsvFmW0knpQ7SO', '1QHf-2SeVdHxGV-3dkyH1Ann0uVtUbU-m', '1XGhHl8ct_n1uwWAsj4yG-Z5yJyJsX1Us']
out=Path(__file__).resolve().parents[1]/'data/raw';out.mkdir(parents=True,exist_ok=True)
for i,id in enumerate(IDS,1):
 p=out/f'source_{i:02d}'
 try: gdown.download(id=id,output=str(p),quiet=False)
 except Exception as e: print('FAILED',id,e)
