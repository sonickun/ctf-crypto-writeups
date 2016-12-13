from fractions import Fraction

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

def continued_fractions(n,e):
	cf = [0]
	while e != 0:
		cf.append(int(n/e))
		N = n
		n = e
		e = N%e
	return cf

def calcKD(cf):
	kd = list()
	for i in range(1,len(cf)+1):
		tmp = Fraction(0)
		for j in cf[1:i][::-1]:
			tmp = 1/(tmp+j)
		kd.append((tmp.numerator,tmp.denominator))
	return kd

def int_sqrt(n):
	def f(prev):
		while True:
			m = (prev + n/prev)/2
			if m >= prev:
				return prev
			prev = m
	return f(n)

def calcPQ(a,b):
	if a*a < 4*b or a < 0:
		return None
	c = int_sqrt(a*a-4*b)
	p = (a + c) /2
	q = (a - c) /2
	if p + q == a and p * q == b:
		return (p,q)
	else:
		return None

def wiener(n,e):
	kd = calcKD(continued_fractions(n,e))
	for (k,d) in kd:
		if k == 0:
			continue
		if (e*d-1) % k != 0:
			continue
		phin = (e*d-1) / k
		if phin >= n:
			continue
		ans = calcPQ(n-phin+1,n)
		if ans is None:
			continue
		return (ans[0],ans[1])

n = 0x9C2F6505899120906E5AFBD755C92FEC429FBA194466F06AAE484FA33CABA720205E94CE9BF5AA527224916D1852AE07915FBC6A3A52045857E0A1224C72A360C01C0CEF388F1693A746D5AFBF318C0ABF027661ACAB54E0290DFA21C3616A498210E2578121D7C23877429331D428D756B957EB41ECAB1EAAD87018C6EA3445
e = 0x466a169e8c14ac89f39b5b0357effc3e2139f9b19e28c1e299f18b54952a07a932ba5ca9f4b93b3eaa5a12c4856981ee1a31a5b47a0068ff081fa3c8c2c546feaa3619fd6ec7dd71c9a2e75f1301ec935f7a5b744a73df34d21c47592e149074a3ccef749ece475e3b6b0c8eecac7c55290ff148e9a29db8480cfe2a57801275

(p,q) = wiener(n,e)

print "p=", str(p)
print "q=", str(q)

f = open("almost_there.encrypted", "r")
ct = int(f.read().encode("hex"), 16)
f.close()

plaintext = decrypt(p, q, e, ct)
print "pass:", plaintext