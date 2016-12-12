# Hack the Vote CTF 2016 : boxes-of-ballots-200

**Category:** Crypto
**Points:**
**Solves:**
**Description:**

> Privjet Komrade! While doing observing of Amerikanski's voting infrascture we find interesting box. We send operative to investigate. He return with partial input like showing below. He say box very buggy but return encrypted data sometimes. Figure out what box is do; maybe we finding embarass material to include in next week bitcoin auction, yes? `ebug\": true, \"data\": \"BBBBBBBBBBBBBBBB\", \"op\": \"enc\"}` `nc boxesofballots.pwn.republican 9001` nauthor's irc nick: Unix-Dude

## Write-up

こちらが指定した平文にFlagを付加してAES-CBC暗号化した結果を返してくる。’A’×ブロック長の暗号文の先頭ブロックを保持しておき、’A’×(ブロック長-1)+xの暗号文の先頭ブロックと一致するようにxをブルートフォースするとFlagが1byte求まる（以下繰り返し）

[solver.py](solver.py)

## Other write-ups and resources

* [Adam Van Prooyen](http://van.prooyen.com/cryptography/2016/11/06/Boxes-of-Ballots-Writeup.html)
* [P4 Team](https://github.com/p4-team/ctf/tree/master/2016-11-05-hack-the-vote/ballots_crypto_200)
* [Carl Loendahl](https://github.com/grocid/CTF/tree/master/Hack%20the%20vote/2016#boxes-of-ballots-200-p)
