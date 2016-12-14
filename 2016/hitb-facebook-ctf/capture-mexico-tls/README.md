# HITB Facebook CTF 2016 : capture Mexico-tls (Crypto200)

**Category:** Crypto
**Points:** ??
**Solves:** ??
**Description:**

> Can you break TLS?
> [Download](tls_16970cb3b09a9dd01f5b82449d9c1795.tar.gz)

## Write-up
TLSで暗号化された通信ログを復号する問題。複数回あるTLSハンドシェイクの中で一度だけエラーが起こっている（CRT exponentが壊れている）ので、RSA-CRT fault Attackを実行して秘密鍵を作成し、HTTPパケットを復号する。

[solver.py](solver.py)

## Other write-ups and resources

