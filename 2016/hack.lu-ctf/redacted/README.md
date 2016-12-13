# Hack.lu CTF 2016 : redacted-200

**Category:** Crypto
**Points:** 200 (-23)
**Solves:** 80
**Description:**

> Someone gave a nice presentation with some redacted ssh keys, I extracted them for you, the seem to belong to berlin@cthulhu.fluxfingers.net on port 1504.
> Good Luck

> Attachment: [redacted](redacted)

## Write-up

RSA秘密鍵読経。PEMキーの一部がマスクされているがhexに直すとe, p, qの値が読めるので秘密鍵が復元できる。作成した鍵でSSHサーバにアクセスするとフラグ。

[command](command)

## Other write-ups and resources

* http://duksctf.github.io/Hack.lu2016-redacted/
* http://manylostticks.blogspot.lu/2016/10/hacklu-ctf-2016-redacted-write-up.html
* https://github.com/ctfs/write-ups-2016/tree/master/hack.lu-ctf-2016/crypto/redacted-200
