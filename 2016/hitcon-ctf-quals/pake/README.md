# HITCON CTF 2016 : pake-250

**Category:** crypto
**Points:** 250
**Solves:**
**Description:**

> nc 52.197.112.79 20431


## Write-up

DH鍵共有単体には認証機能がなくMITMに対して脆弱なため、PAKE(Password Authenticated Key Exchange)が使われているが、Passwordが総当たり可能なので認証を突破できる。

[solver.py](solver.py)


## Other write-ups and resources

* none yet
