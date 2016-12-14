# H4ckIT CTF 2016 : ninja-scheme-195

**Category:** crypto
**Points:**
**Solves:**
**Description:**

Chad

> General Tompson welcomes you...again! We have some crypto-problem here...again. Our scouts have intercepted this enemy cryptogram:  dd67ca82d358f0c8479e118addcec2f8ce086c0f6f239f9b66d7226a38c68198dbd777f366fb9fd83b60d11109be174759c75ea56a4866c2 Some time later our IT-ninjas have broken into the enemy computer system and grabbed something pretty much similar to undefined encryption algorithm scheme. Look at this grabbed scheme and help us to understand how it works. Yours, Gen. Tompson

## Write-up

![](Smth_prEtTy_s1mil4r_t0_crYpto_scCHem3_f536e2a0a525f61af5579c5b34fbe045.png)

独自のFeistel構造を持つブロック暗号を解読する問題。復号処理を実装し、keyがラウンド数に等しいと仮定してラウンド数をブルートフォースすると既知の平文に復号でき、keyが求まる。

[solver.py](solver.py)

## Other write-ups and resources

* none yet
