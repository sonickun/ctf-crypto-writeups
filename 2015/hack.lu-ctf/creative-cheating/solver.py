# Hack.lu CTF 2016 Creative Cheating (Crypto 150pt)

def egcd(a, b):
 if (a == 0):
     return [b, 0, 1]
 else:
     g, y, x = egcd(b % a, a)
     return [g, x - (b // a) * y, y]

def modInv(a, m):
 g, x, y = egcd(a, m)
 if (g != 1):
     raise Exception("[-]No modular multiplicative inverse of %d under modulus %d" % (a, m))
 else:
     return x % m

def decrypt(p, q, e, c):
	n = p * q
	phi = (p - 1) * (q - 1)
	d = modInv(e, phi)
	m = pow(c, d, n)
	return m

def verify(Bm, sig):
	An = 0x53a121a11e36d7a84dde3f5d73cf
	# Ap = 38456719616722997
	# Aq = 44106885765559411
	Ae = 0x10001
	Am = pow(sig, Ae, An)
	return Am == Bm


Bp = 49662237675630289
Bq = 62515288803124247
Be = 0x10001

f = open("dump.txt", "r")

flist = []
for line in f:
	line = line.strip().decode("base64")
	row = line.split(" ")
	seq = int(row[2][:-1])
	data = int(row[5][:-2], 16)
	sig = int(row[8][:-2], 16)
	# print seq, data, sig
	m = decrypt(Bp, Bq, Be, data)
	if verify(m, sig) == True:
		plain = hex(m)[2:-1].zfill(2).decode("hex")
		flist.append([seq, plain])
f.close()

flist.sort(key=lambda x:x[0])

flag = ""
for f in flist:
	flag += f[1]
print flag

# Result
# >python solver.py
# flag{n0th1ng_t0_533_h3r3_m0v3_0n}