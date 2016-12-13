import socket
import hashlib
import itertools

def hash_solve(s):
	charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	for i in range(5):
		for j in itertools.product(charset, repeat=i):
			test = "".join(j)
			h = hashlib.md5(test).hexdigest().strip()
			if h[:5] == s:
				break
	return test


def check(coefs, solution, target):
	check = sum([solution[i]*coefs[i] for i in range(6)]) % 8
	for v in [-1, 0, 1]:
		result = (check + 8 + v) % 8
		if result == target:
			return True
	return False

s = socket.socket()
s.connect(("localhost", 8888))

data = s.recv(1024)
print data
challenge = data.split(" = ")[1].strip()

ans = hash_solve(challenge)
print "ans", ans
s.send(ans + "\n")

data = s.recv(1024)
data += s.recv(4096)
g = data.split("\n")[:-2]

for k in itertools.product(range(8), repeat=6):
	truecount = 0
	for line in g:
		coefs = map(int, line.split(", ")[:6])
		result = int(line.split(", ")[-1])
		if check(coefs, k, result):
			truecount += 1
	if truecount > 30:
		output = "%s\n" % (", ".join(map(str, k)))
		print output
		s.send(output)
		data = s.recv(1024)
		print data
		data = s.recv(1024)
		print data

s.close()