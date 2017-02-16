from Crypto.Util.number import *
import gmpy

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
    #return hex(pt)[2:-1].decode("hex")
    return pt
    
n = 0xD8E24C12B7B99EFE0A9BC04A6A3DF58A2A944269B492B7376DF129023F2061B9
e = 0xac2ac3e0ca0f5607

p = 311155972145869391293781528370734636009
q = 315274063651866931016337573625089033553

print p * q == n


c = open("flag.enc").read().decode("base64")
c = bytes_to_long(c)
print size(c)

while True:
    n = p * q
    print size(n)
    if c < n:
        break
    else:
        p = gmpy.next_prime(p**2 + q**2)
        q = gmpy.next_prime(2*p*q)
        e = gmpy.next_prime(e**2)

print p, q, e
m = decrypt(p, q, e, c)
print m
print long_to_bytes(m)

# ASIS{F4ct0R__N_by_it3rat!ng!}
