# Hack.lu CTF 2016 : cornelius-1-200

**Category:** Crypto
**Points:** 200 (-29)
**Solves:**
**Description:**

> Please find Cthulhu's magic [here](https://cthulhu.fluxfingers.net:1505/).
> Attachment: [server.rb](server.rb)
> P.S.: flag is the content of the file and is not in flagformat!

## Write-up

Webサーバの認証情報（フラグ）をdeflate圧縮した上にAES-CTRで暗号化している。deflate圧縮にはCRIME脆弱性があるので、既知の平文とフラグの候補を送りデータの圧縮率の違いを見ながらフラグを特定できる。

[solver.py](solver.py)

## Other write-ups and resources

* http://anee.me/hack-lu-ctf-2016-cornelius1-writeup/
