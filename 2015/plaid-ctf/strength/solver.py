# GCD (times sign of b if b is nonzero, times sign of a if b is zero)
def gcd(a,b):
 while b != 0:
     a,b = b, a % b
 return a

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


crypt = []
f = open("captured_827a1815859149337d928a8a2c88f89f.txt","r")

for line in f:
    if ("N" not in line):
        line = line.strip().replace("L","").replace("{","").replace("}","")
        row = line.strip().split(" : ")
        row = [long(x.strip(),16) for x in row]
        crypt.append(row)

for x in crypt:
    for y in crypt:
        if(x == y):
            continue

        if(gcd(x[1],y[1]) == 1):
            n = x[0]
            a = egcd(x[1], y[1])
            if(a[1] < 0):
                x[2] = modInv(x[2], n)
                a[1] = a[1] * -1
            else:
                y[2] = modInv(y[2], n)
                a[2] = a[2] * -1

            m = (pow(x[2],a[1],n) * pow(y[2],a[2],n)) % n
            print hex(m)[2:-1].decode('hex')
            exit()

f.close()
