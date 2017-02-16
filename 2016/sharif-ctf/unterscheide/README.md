# Sharif 2016 : unterscheide-200

**Category:** Sharif-Ctf-2016
**Points:** 
**Solves:** 
**Description:**

> See the attachment [Download](<http://ctf.sharif.edu/ctf7/api/download/27)>


## Write-up

FlagをAES-CBCで暗号化し、さらに暗号文のbitごとに乱数を使って暗号化している。フェルマーの小定理やらなんやらを使って数式を殴るとAESの暗号文や暗号鍵を復元できる。

[solver.py](solver.py)

## Other write-ups and resources

* none yet
