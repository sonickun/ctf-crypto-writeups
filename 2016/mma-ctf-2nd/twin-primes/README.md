# MMA CTF 2nd 2016 : twin-primes-50

**Category:** Crypto Warmup
**Points:** 50
**Solves:** 183
**Description:**

> Decrypt it.
>
> [[twin-primes.7z](./twin-primes.7z)]([twin-primes.7z](./twin-primes.7z))


## Write-up

双子素数のペアを２つ使って鍵を２つ作り、２重にRSA暗号化している。公開鍵としてp\_qと(p+2)\_(q+2)の値が分かっているので式変形エンヤコラして秘密鍵を求め復号する。

[solver.py](solver.py)

## Other write-ups and resources

* https://github.com/TeamContagion/CTF-Write-Ups/tree/master/TokyoWesterns-2016/Twin%20Primes
* [Invulnerable (Russian)](http://countersite.org/articles/cryptography/113-twin-primes-writeup.html)
* http://hamidx9.ir/solutions/2016/tw_mma_ctf/twin_primes/sol.py
* http://shpik.tistory.com/71
* https://github.com/ByteBandits/writeups/tree/master/mma-ctf-2016/crypto/twin-primes/sudhackar
* http://megabeets.net/twctf-2016-crypto-twin-primes/
