# MMA CTF 2nd 2016 : esper-180

**Category:** Crypto
**Points:** 180
**Solves:** 30
**Description:**

> Are you an ESPer?
>
>
> nc cry1.chal.ctf.westerns.tokyo 37992


## Write-up

RSAの暗号化・復号処理で一度だけ任意の変数を任意のタイミングで破壊する(乱数に置き換える)ことができる。復号処理で高速化のために中国人剰余定理を使って計算しているので、片方のPrivate Exponentを書き換えてRSA-CRT Fault Attackを実行し秘密鍵を得る

[solver.py](solver.py)

## Other write-ups and resources

* [0x90r00t (French)](https://0x90r00t.com/fr/2016/09/08/mma-ctf-2016-crypto-180-esper-write-up/)
* (Vietnamese) https://quandqn.wordpress.com/2016/09/05/tokyo-westernsmma-ctf-2nd-2016-twin-primes-esper/
