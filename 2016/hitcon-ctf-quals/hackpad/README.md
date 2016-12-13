# HITCON CTF 2016 : hackpad-150

**Category:** forensics
**Points:** 150
**Solves:**
**Description:**

> My site was hacked. The secret was leaked.


## Write-up

CBCモードに対するPadding Oracle Attackの通信ログが渡される。復号が成功したとき（ステータスコード200）の時の攻撃ブロックを取り出して攻撃を再現し平文を得る。

[solver.py](solver.py)

## Other write-ups and resources

* http://crypto.rop.sh/post/UCYDL42CB9UN
* https://jiulongw.github.io/post/hitcon-2016-hackpad/
* https://gophers-in-the-shell.herokuapp.com/hitcon-2016-hackpad-crypto-forensics-150pts/
