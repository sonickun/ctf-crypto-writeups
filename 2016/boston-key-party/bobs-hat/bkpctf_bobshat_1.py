import math

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
		gcd = b
	return gcd, x, y

def decrypt(p, q, e, ct):
	n = p * q
	phi = (p - 1) * (q - 1)
	gcd, a, b = egcd(e, phi)
	d = a
	pt = pow(ct, d, n)
	return hex(pt)[2:-1].decode("hex")

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n):
	x = isqrt(n) + 1
	y = isqrt(x * x - n)

	while True:
		w = x * x - n - y * y
		if w == 0:
			break
		elif w > 0:
			y += 1
		else:
			x += 1
	return x+y, x-y


n = 0x86E996013E77C41699000E0941D480C046B2F71A4F95B350AC1A4D426372923D8A4561D96FBFB0240595907201AD3225CF6EDED7DE02D91C386FFAC280B72D0F95CAE71F42EBE0D3EDAEACE7CEA3195FA32C1C6080D90EF853D06DD4572C92B9F8310BBC0C635A5E26952511751030A6590816554E763031BCBB31E3F119C65F
e = 65537

p, q = fermat(n)

print "p=", str(p)
print "q=", str(q)

f = open("almost_almost_almost_almost_there.encrypted", "r")
ct = int(f.read().encode("hex"), 16)
f.close()

plaintext = decrypt(p, q, e, ct)
print "pass:", plaintext