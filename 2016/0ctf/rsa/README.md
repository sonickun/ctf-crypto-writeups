# 0CTF : rsa-2

**Category:** Crypto
**Points:** 2
**Solves:** 32
**Description:**

> It seems easy, right?
>
> Tip: openssl rsautl -encrypt -in FLAG -inkey public.pem -pubin -out flag.enc
>


## Write-up

一見 Multiprime RSA に見えるがφ(N)とeが互いに素でないので拡張ユークリッド互除法で秘密鍵dが計算できない。一方、eの値が3と非常に小さいため、中国剰余定理を用いてLow Public Exponent Attack(もどき)が適用でき、平文の候補が求まる。

[solver.py](solver.py)


## Other write-ups and resources

* [P4 Team](https://github.com/p4-team/ctf/tree/master/2016-03-12-0ctf/rsa)
