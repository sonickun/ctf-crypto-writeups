import fractions

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


prev_n = 0x86E996013E77C41699000E0941D480C046B2F71A4F95B350AC1A4D426372923D8A4561D96FBFB0240595907201AD3225CF6EDED7DE02D91C386FFAC280B72D0F95CAE71F42EBE0D3EDAEACE7CEA3195FA32C1C6080D90EF853D06DD4572C92B9F8310BBC0C635A5E26952511751030A6590816554E763031BCBB31E3F119C65F
n = 0xABE633CEC2E7EC10A851927905A657DF4E10416023C0C34FC64D64BD8B8257B7BF207ADD047B0ADF21C525B052068C70295C746C3B1BE1436F39ED8BF7A813E4B845CE0CA89CA828B45763D46B1898C7A2FA5F8FE78428CAB6CDF70EF871DB971B3232841A1CE2459CE650A154362F80CFB64163C3CA63AD72BCFBDBF0154FF7
e = 65537

p = fractions.gcd(prev_n, n)
q = n / p

print "p=", str(p)
print "q=", str(q)

f = open("almost_almost_almost_there.encrypted", "r")
ct = int(f.read().encode("hex"), 16)
f.close()

plaintext = decrypt(p, q, e, ct)
print "pass:", plaintext