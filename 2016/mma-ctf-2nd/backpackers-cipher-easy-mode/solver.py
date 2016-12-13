import json
import Crypto.Cipher.DES as DES
import struct
from Crypto.Util.number import *

# Extended Greatest Common Divisor
def egcd(a, b):
 if (a == 0):
     return [b, 0, 1]
 else:
     g, y, x = egcd(b % a, a)
     return [g, x - (b // a) * y, y]

# Modular multiplicative inverse
def modInv(a, m):
 g, x, y = egcd(a, m)
 if (g != 1):
     raise Exception("[-]No modular multiplicative inverse of %d under modulus %d" % (a, m))
 else:
     return x % m

f = open("pubkey")
N = json.load(f)
f.close()

p = N[1022] * 2 - N[1023]

q = (N[1023] * modInv(2**1023, p)) % p

assert N[1023] == (2**1023 * q) % p

print "[+] p:", p
print "[+] q:", q

c = 92649594207825438717837187204344278404540834511527089878910723459724389288678038170396293259249677359505828960485220701331410243786492001840574936432405740788287474436598857182135645351292417701523146725619033398034087168810420579428717317863390516995362334697735659981180212183075160527597025256459439474027758405

c = (c * modInv(q, p)) % p
x = ""

for i in range(len(N)):
    s = bin(c)[2:]
    if c % 2**(i+1):
        x += "1"
        w = (N[i] * modInv(q, p)) % p
        c -= w
    else:
        x += "0"

message = long_to_bytes(int(x, 2))

CRYPTO_KEY = "testpass"
crypto_object = DES.new(CRYPTO_KEY, DES.MODE_ECB)
plain = crypto_object.decrypt(message)

print plain

# flag: Flag:TWCTF{ESC4P3FR0MPR1SON}