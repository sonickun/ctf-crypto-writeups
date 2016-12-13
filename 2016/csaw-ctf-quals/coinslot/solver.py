import socket

remoteip   = "misc.chal.csaw.io"
remoteport = 8000

def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

s, f = sock(remoteip, remoteport)

def solve(target):
	target = int(round(target * 100, 0))
	bills = [10000, 5000, 1000, 500, 100, 50, 20, 10, 5, 1,
		0.5, 0.25, 0.1, 0.05, 0.01]
	ans = ""
	for bi in bills:
		bi = int(bi * 100)
		num = target // bi
		ans += (str(num) + "\n")
		target = target % bi
	s.send(ans)
	read_until(f, "(1c): ")
	print read_until(f, "!\n")

count = 0
while True:
	print "[+] Iter:", count
	line = read_until(f, "\n")
	print line,
	target = float(line.replace("$", "").strip())
	print "[+] target:", target
	solve(target)
	count += 1

s.close()

# flag: flag{started-from-the-bottom-now-my-whole-team-fucking-here}