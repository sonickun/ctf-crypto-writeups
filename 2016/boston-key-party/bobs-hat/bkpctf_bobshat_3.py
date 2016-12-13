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

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


def small_prime(modulus):
	i = 1
	while True:
		if is_prime(i):
			if modulus % i == 0:
				return i, modulus/i
		else:
			pass
		i += 1

n = 0xBAD20CF97ED5042DF696CE4DF3E5A678CF4FB3693D3DF12DFE9FD3FD8CC8AAB8B95533E414E3FC0C377F4EE54827118B1D30561A3C741BEA7C76899789B51743E076092DF9EB05DC97EB1505CE9EB12B5AB9E10ABF56F920A58E7E00ECF05977E872834DD8584CF4AC87CB7DC50159BD962C75CBEFB6C6AC3A31A74E7D8F1E4C10D5
e = 65537

p, q = small_prime(n)

print "p=", str(p)
print "q=", str(q)

f = open("almost_almost_there.encrypted", "r")
ct = int(f.read().encode("hex"), 16)
f.close()

plaintext = decrypt(p, q, e, ct)
print "pass:", plaintext