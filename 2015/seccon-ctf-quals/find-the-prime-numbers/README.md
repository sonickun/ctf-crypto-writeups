# SECCON Quals CTF 2015: Find the prime numbers

**Category:** Crypto
**Points:** 200
**Solves:** 54
**Description:**

> $ cp [pq.cgi](./pq.cgi) /var/www/[pq.cgi](./pq.cgi).txt
> 
> <http://pailler.quals.seccon.jp/[pq.cgi](./pq.cgi).txt>
> 
> <http://pailler.quals.seccon.jp/cgi-bin/[pq.cgi](./pq.cgi)>


## Write-up

とある暗号の実装と暗号文を含む3数が与えられる。実装から加法準同型暗号の一つであるPaillier暗号だと分かる。3数の定義より素因数分解を用いて秘密鍵の候補となる素数が計算できる(複数のデータセットを用いて特定)。後はPaillierの復号方法に則ってコードを書き平文を求める。

[solver.py](solver.py)

## Other write-ups and resources

* <https://github.com/p4-team/ctf/tree/master/2015-12-05-seccon/paillier_crypto_200#eng-version>
* [Japanese](https://hackmd.io/s/VJ42d6j4e)
* [Japanese](http://www.iridoatelier.net/sb/log/eid269.html)
