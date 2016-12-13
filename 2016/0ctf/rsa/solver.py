# -*- coding:utf-8 -*-
# 0CTF 2016: RSA? (Crypto 2pt)

'''
# openssl rsa -in public.pem -pubin -text -modulus
Public-Key: (314 bit)
Modulus:
    02:ca:a9:c0:9d:c1:06:1e:50:7e:5b:7f:39:dd:e3:
    45:5f:cf:e1:27:a2:c6:9b:62:1c:83:fd:9d:3d:3e:
    aa:3a:ac:42:14:7c:d7:18:8c:53
Exponent: 3 (0x3)
Modulus=2CAA9C09DC1061E507E5B7F39DDE3455FCFE127A2C69B621C83FD9D3D3EAA3AAC42147CD7188C53
writing RSA key
-----BEGIN PUBLIC KEY-----
MEEwDQYJKoZIhvcNAQEBBQADMAAwLQIoAsqpwJ3BBh5Qflt/Od3jRV/P4Seixpti
HIP9nT0+qjqsQhR81xiMUwIBAw==
-----END PUBLIC KEY-----

'''

# Chinese Remainder Theorem
def chinese_remainder(n, a):
	sum = 0
	prod = reduce(lambda a, b: a*b, n)
	for n_i, a_i in zip(n, a):
		p = prod / n_i
		sum += a_i * mul_inv(p, n_i) * p
	return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


e = 3
n = 0x2CAA9C09DC1061E507E5B7F39DDE3455FCFE127A2C69B621C83FD9D3D3EAA3AAC42147CD7188C53

# Factorize n using factordb.com
p = 26440615366395242196516853423447
q = 27038194053540661979045656526063
r = 32581479300404876772405716877547

assert p * q * r == n

ct = int(open("flag.enc", "rb").read().encode("hex"), 16)
# ct = 2485360255306619684345131431867350432205477625621366642887752720125176463993839766742234027524

# pt^3 mod p = ct mod p = 20827907988103030784078915883129
# pt^3 mod q = ct mod q = 19342563376936634263836075415482
# pt^3 mod r = ct mod r = 10525283947807760227880406671000

# Calculate possible cube-root 
# using wolflam alpha (or using modified Tonelli-Shanks algorithm)
# like this: "x^3 = 20827907988103030784078915883129 (mod 26440615366395242196516853423447)"
p_root = [5686385026105901867473638678946, 7379361747422713811654086477766, 13374868592866626517389128266735]
q_root = [19616973567618515464515107624812]
r_root = [6149264605288583791069539134541, 13028011585706956936052628027629, 13404203109409336045283549715377]

# For every compination of roots, mix them using Chinese Remainder Theorem
for x in p_root:
	for y in q_root:
		for z in r_root:
			m = chinese_remainder([p, q, r], [x, y, z])
			pt = hex(m)[2:-1]
			if len(pt) % 2 != 0:
				pt = "0"+pt
			pt = pt.decode("hex")
			if pt.find("0ctf{") >= 0:
				# Get the flag
				print pt.strip()
				break

# Result
# > python solver.py
# �^˄�RC�J0ctf{HahA!Thi5_1s_n0T_rSa~}