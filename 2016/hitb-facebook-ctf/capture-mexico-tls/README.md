# HITB Facebook CTF 2016 : capture Mexico-tls (Crypto200)

**Category:** Crypto
**Points:** ??
**Solves:** ??
**Description:**

> Can you break TLS?
> [Download](tls_16970cb3b09a9dd01f5b82449d9c1795.tar.gz)

## Write-up
8文字のkeyを2文字ずつ4分割してSHA-256でハッシュ化し、それぞれをkeyとしてAES-CBCで4回暗号化を重ねている。2文字ずつブルートフォースして復号結果のパディング長が正しい値になるかをチェックしてkeyを特定していく。

[solver.py](solver.py)

## Other write-ups and resources

