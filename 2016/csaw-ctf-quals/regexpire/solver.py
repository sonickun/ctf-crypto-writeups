import socket
import rstr

remoteip   = "misc.chal.csaw.io"
remoteport = 8001

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

print read_until(f, "regexes?\n")

count = 0
while True:
	print "[+] Iter:", count
	target = read_until(f, "\n").strip()
	print "[+] Target:", target

	ans = rstr.xeger(target)
	while '\n' in ans:
		ans = rstr.xeger(target)
	print "[+] Answer:", ans
	s.send(ans+"\n")
	count += 1
	
s.close()

#flag: flag{^regularly_express_yourself$}