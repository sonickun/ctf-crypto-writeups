# Sharif University CTF 2016 : High-speed RSA Keygen

**Category:** Crypto
**Points:** 150
**Solves:** 25
**Description:**

> See the attached files.
> 
> Download [RSA-Keygen.tar.gz](./RSA-Keygen.tar.gz)


## Write-up

RSAの鍵(素数)生成のコードが渡されるが実装が甘く、1024bit素数の上位約2/3のビットが高々2^12回の試行で総当たりできる。残りのビットが完全にランダムと考えると、Coppersmithの定理を用いてHigh-bit Known Attackが実行でき、素数が求まる。

[sover.py](solve.py)  
[decrypt.py](decrypt.py)

## Other write-ups and resources

* [Korean](https://github.com/tyhan/CTF/tree/master/SharifCTF2016/High-speed_RSA_Keygen)
* https://gist.github.com/elliptic-shiho/4e3d6bac91a032cc6f20
