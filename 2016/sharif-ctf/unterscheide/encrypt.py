#!/usr/bin/python
 
import gmpy
import random, os
from Crypto.Util.number import *
from Crypto.Cipher import AES
 
from secret import flag, q, p1, p2, h
 
assert (gmpy.is_prime(q) == 0) + (q-1) % p1 + (q-1) % p2 + (p2 - p1 > 10**8) + (pow(h, 1023*p1*p2, q) == 1) == 0
 
key = os.urandom(128)
IV = key[16:32]
mode = AES.MODE_CBC
aes = AES.new(key[:16], mode, IV=IV)
flag_enc = aes.encrypt(flag)
 
rand = bytes_to_long(key)
benc = bin(bytes_to_long(flag_enc))[2:]
 
A = []
for b in benc:
    try:
        r = gmpy.next_prime(random.randint(3, q-2))
        s = gmpy.invert(r, q-1)
        if b == '0':
            a = pow(h, r*r*p1, q)*q*rand + rand + 1
        else:
            a = pow(h, s*s*p2, q)*q*rand + rand + 1
        A.append(str(int(a)))
        rand += 1
    except:
        print 'Failed'
 
fenc = open('enc.txt', 'w')
fenc.write('\n'.join(A))
fenc.close()
