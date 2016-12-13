from sage.all import import *

def ntopoly(npoly):
        return sum(c*X**e for e, c in enumerate(Integer(npoly).bits()))

def polyton(poly):
        return sum(int(poly[i])*(1 << i) for i in xrange(poly.degree() + 1))

X = GF(2).polynomial_ring().gen()

INNER = ntopoly(0x3636363636363636)
OUTER = ntopoly(0x5c5c5c5c5c5c5c5c)
CRC_POLY = ntopoly((2**64) + 0xeff67c77d13835f7)
CONST = ntopoly(0xabaddeadbeef1dea)
HMAC_CRC = ntopoly(0xa57d43a032feb286)
m = ntopoly(int("zupe zecret".encode("hex"), 16))
M = 88

k = (HMAC_CRC - (OUTER*X^128 + INNER*X^(M+128) + m*X^128 + CONST*(X^64+1)))
k = k * inverse_mod(X^128 + X^(M+128), CRC_POLY)
k = k % CRC_POLY

print hex(polyton(k))

