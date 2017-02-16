# ASIS CTF Finals 2016 : rsa-113

**Category:** Crypto
**Points:** 113
**Solves:** 64
**Description:**

Find the [flag](rsa.txz).

## Write-up

RSA暗号。鍵長が短くn < plaintext となり暗号化でエラーが起きるため、pと
qを更新して徐々に大きくしている。最初のnは容易に素因数分解可能なのでn > plaintext となる最初のp,qを見つけて復号する。
[solver.py](solver.py)

## Other write-ups and resources

* [P4 Team](https://github.com/p4-team/ctf/tree/master/2016-09-09-asis-final/rsa)
* https://kinyabitch.wordpress.com/2016/09/11/asis-ctf-finals-rsa/
