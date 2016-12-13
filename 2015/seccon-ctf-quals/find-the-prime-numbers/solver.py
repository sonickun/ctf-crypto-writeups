# SECCON CTF 2015 Online Quals Find the prime numbers (Crypto 200pt)

def egcd(a, b):
 if (a == 0):
     return [b, 0, 1]
 else:
     g, y, x = egcd(b % a, a)
     return [g, x - (b // a) * y, y]

# Modular multiplicative inverse
def modInv(a, m):
 g, x, y = egcd(a, m)
 if (g != 1):
     raise Exception("[-]No modular multiplicative inverse of %d under modulus %d" % (a, m))
 else:
     return x % m

def L(u, n):
	return (u - 1) / n

# c + o = h
# 2312852200158242541 + 3960472713339509644 = 1680683066780585790
c = 2312852200158242541
o = 3960472713339509644
h = 1680683066780585790

# h = o * c mod n^2
# Get factors of "o*c-h"
# 2 * 3^3 * 42727^2 * 58757^2 * 664253 * 40517588857
p = 42727
q = 58757

n = p * q
ramda = (p - 1) * (q - 1)

l = pow(c, ramda, n * n)

# g = 1 + n (mod n^2)
# mu = L(g^ramda mod n^2) (mod n)
#    = ramda (mod n)
ramda_inv = modInv(ramda, n)

m = (L(l, n) * ramda_inv) % n

print m

# Result
# > python solver.py
# 1510490612

# Access: http://paillar.quals.seccon.jp/cgi-bin/pq.cgi?1510490612 
# Flag: SECCON{SECCoooo_oooOooo_ooooooooN}
