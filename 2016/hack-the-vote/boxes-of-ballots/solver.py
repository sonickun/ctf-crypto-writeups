import socket
import string
import time

flag_len = 23

remoteip   = "boxesofballots.pwn.republican"
remoteport = 9001

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"

def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

flag = ""

for i in range(flag_len):
	s, f = sock(remoteip, remoteport)
	send_data = '{"data": "%s", "op": "enc"}' % ('A'*(31-i))
	s.send(send_data + "\n")
	stream = read_until(f, "}")
	cipher = stream.split('"')[-2]
	first_block = cipher[:64]
	print "[*] first_block:", first_block
	s.close()

	for c in charset:
		s, f = sock(remoteip, remoteport)
		send_data = '{"data": "%s%c", "op": "enc"}' % ('A'*(31-i)+flag, c)
		print "send", send_data
		s.send(send_data + "\n")
		stream = read_until(f, "}")
		cipher = stream.split('"')[-2]
		if cipher[:64] == first_block:
			flag = flag + c
			print "[*] FLAG: %s" % flag
			break
		s.close()
	print 

# [*] FLAG: flag{Source_iz_4_noobs}
