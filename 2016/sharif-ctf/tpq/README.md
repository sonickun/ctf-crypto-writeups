# Sharif 2016 : tpq-150

**Category:** Sharif-Ctf-2016
**Points:**
**Solves:**
**Description:**

> nc ctf.sharif.edu 4000


## Write-up

ランダムに生成された10個の素数のうち2つを選択し，FlagをRSA暗号化したものを得る．
計算式をうまく変形すると素数が求まる．

```
c01 = m^e - k1p0p1
c02 = m^e - k2p0p2
c03 = m^e - k3p0p3

c01 - c02 = p0(k2p2 - k1p1)
c02 - c03 = p0(k3p3 - k2p2)

p0 = gcd(c01 - c02, c02 - c03)
```

[solver.py](solver.py)

## Other write-ups and resources

*
