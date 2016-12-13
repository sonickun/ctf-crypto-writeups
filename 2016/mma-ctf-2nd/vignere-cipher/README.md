# MMA CTF 2nd 2016 : vigenere-cipher-200

**Category:** Crypto
**Points:** 200
**Solves:** 30
**Description:**

> [[vigenere.7z](./vigenere.7z)]([vigenere.7z](./vigenere.7z))


## Write-up

ヴィジュネル暗号×Base64。カシスキーテストで鍵長を求める。平文がエンコードされてて頻度分析ができないので、「平文3文字とBase64 4文字が対応すること」と「鍵は複数回使いまわされること」を利用して復号結果がASCII文字になるように鍵をブロックに分けて総当たりする。

[solver.py](solver.py)

## Other write-ups and resources

* none yet
