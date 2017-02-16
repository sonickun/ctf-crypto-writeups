import gmpy
from Crypto.Util.number import *
from Crypto.Cipher import AES

f = open("enc.txt", "r")

A = []
for line in f:
    a = int(line.strip())
    A.append(a)
 
f.close()

X = [A[i]-A[i-1]-1 for i in xrange(1, len(A))]
q = X[0]
for x in X:
    q = gmpy.gcd(q, x)

assert gmpy.is_prime(q)

print "[+]q:", q
# p = 2 * p1 * p2 -1
p1 = 9090368507916642523150386537322321669636426087368916042946887058939035329547274618743911402935105936038626517888669029591219526735351668782037241434579031 
p2 = 9090368507916642523150386537322321669636426087368916042946887058939035329547274618743911402935105936038626517888669029591219526735351668782037241444579211
print "[+]p1:", p1
print "[+]p2:", p2
assert  (p2 - p1 > 10**8) == 0

rand = (A[0] % q) - 1
print "[+]rand:", rand

bits = ""
for i, a in enumerate(A):
    m = (a-(rand+i+1))/(q*(rand+i))
    if pow(m, 2*p2, q) == 1:
        bits += '0'
    elif pow(m, 2*p1, q) == 1:
        bits += '1'
    else:
        print "error"
        exit()

benc = long_to_bytes(int(bits, 2))

key = long_to_bytes(rand)[:16]
IV = long_to_bytes(rand)[16:32]
aes = AES.new(key, AES.MODE_CBC, IV=IV)
flag = aes.decrypt(benc)

print flag
