import socket
import hashlib
import telnetlib
import fractions

# nc cry1.chal.ctf.westerns.tokyo 37992
remoteip   = "cry1.chal.ctf.westerns.tokyo"
remoteport = 37992

def shell(s):
	t = telnetlib.Telnet()
	t.sock = s
	t.interact()

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

s, f = sock(remoteip, remoteport)
read_until(f, "\n")
line = read_until(f, "\n")

x = int(line.strip().split(" ")[-5])
y = int(line.strip().split(" ")[-1])

print "[+] start:", x
print "[+] end:", y

number = x

while True:
	if hashlib.sha1(str(number)).hexdigest().startswith('00000') == True:
		print "[+] Found:", number
		break
	elif number == y:
		print "not found"
		break
	else:
		number += 1

e = 65537

s.send(str(number)+"\n")
# shell(s)	

read_until(f, ">")
s.send("1\n")
read_until(f, ":")
s.send("\n")
read_until(f, ":")
s.send("2\n")
line = read_until(f, ">")
a = int(line.strip().split("\n")[0].split(" ")[-1])
print "[+] 2^e mod n:", a 

s.send(str(number)+"\n")
read_until(f, ">")
s.send("1\n")
read_until(f, ":")
s.send("\n")
read_until(f, ":")
s.send("3\n")
line = read_until(f, ">")

b = int(line.strip().split("\n")[0].split(" ")[-1])
print "[+] 3^e mod n:", b 

n = fractions.gcd(pow(2,e)-a, pow(3,e)-b)
print "[+] n:", n

s.send("2\n")
read_until(f, ":")
s.send("5:dp\n")
read_until(f, ":")
s.send(str(a)+"\n")
read_until(f, "Decrypted:")
line = read_until(f, "\n")
fault = int(line.strip())
print "[+] Fault:", fault

read_until(f, "here.\n")
line = read_until(f, "\n")
c = int(line.strip())
print "[+] Cipher:", c

p = fractions.gcd(fault-2, n)
q = n / p

print "[+] p:", p
print "[+] q:", q

m = decrypt(p, q, e, c)
print "[+] m:", m
print hex(m)[2:-1].decode("hex")

s.close()

# Flag: TWCTF{I_don't_Lik3_ESPer_problems!}