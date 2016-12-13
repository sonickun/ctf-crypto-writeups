# MMA CTF 2nd 2016 : super-express-100

**Category:** Crypto
**Points:** 100
**Solves:** 155
**Description:**

> [[super_express.7z](./super_express.7z)]([super_express.7z](./super_express.7z))


## Write-up

鍵を使って平文を一文字ずつ変換していく換字式暗号。鍵の長さに応じて変換の回数が変化するが、変換は線形写像であり、何度繰り返しても同じ形の式になるので、高々１回分の鍵のパターンを当てるのと同じ難易度。

[solver.py](solver.py)

## Other write-ups and resources

* https://github.com/ByteBandits/writeups/tree/master/mma-ctf-2016/crypto/super-express/sudhackar
