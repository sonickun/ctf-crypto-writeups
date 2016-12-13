# MMA CTF 2nd 2016 : backpackers-cipher-easy-mode-200

**Category:** Crypto
**Points:** 200 
**Solves:** 19
**Description:**

> Decrypt it. [[backpack.7z](./backpack.7z)]([backpack.7z](./backpack.7z))


## Write-up

前半はMerkle-Hellmanナップサック暗号もどき。秘密鍵が超増加列ではないので普通の方法では復号できない。鍵生成に問題があり、下位ビットが初めて1になる位置がわかることを利用して、1bitずつメッセージを復元できる。後半はDESで復号するだけ。鍵生成において後ろの公開鍵になるほど候補が狭まるのでp,qが求まる。

[solver.py](solver.py)

## Other write-ups and resources

* none yet
