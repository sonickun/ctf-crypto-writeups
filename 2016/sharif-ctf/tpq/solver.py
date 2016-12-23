import socket
from fractions import gcd
from Crypto.Util.number import long_to_bytes
from gmpy import is_prime

remoteip   = "ctf.sharif.edu"
remoteport = 4000

def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def get_cipher(s, f, a, b):
    read_until(f, "uit.\n")
    s.send("C\n")
    read_until(f, "space.\n")
    s.send("%d %d\n" % (a, b))
    cipher = long(read_until(f, "\n").strip().split(" ")[-1])
    return cipher


e = 65537
s, f = sock(remoteip, remoteport)

c01 = get_cipher(s, f, 0, 1)
c02 = get_cipher(s, f, 0, 2)
c03 = get_cipher(s, f, 0, 3)
p = gcd(abs(c01 - c02), abs(c02 - c03))
assert is_prime(p)
print "p", p

c12 = get_cipher(s, f, 1, 2)
c13 = get_cipher(s, f, 1, 3)
c14 = get_cipher(s, f, 1, 4)
q = gcd(abs(c12 - c13), abs(c13 - c14))
assert is_prime(q)
print "q", q

n = p * q
phi = (p-1) * (q-1)
gcd, a, b = egcd(e, phi)
d = a
pt = pow(c01, d, n)
print long_to_bytes(pt)

s.close()

# p 12444626242275143650937913975275793151277215354986741592253673629340453453487059162502062847141751866548776848925514654255746588109753692793664545052450789
# q 10987262138872864911926043077280792546550601146758406919344438374048884109295778717264484332554115247467677709289591677377733564206946877818638588880842447
# SharifCTF{7c62f12e7e6f08f9f5365e45588d34d8}
