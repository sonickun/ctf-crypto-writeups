import socket
from Crypto.Util.number import long_to_bytes
from hashlib import sha512

remoteip   = "133.9.81.203"
remoteport = 1337

def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

def get_bb(f):
    read_until(f, "send ")
    bb = int(read_until(f))
    return bb

def get_enc(f):
    read_until(f, ": ")
    enc = int(read_until(f))
    return enc

def get_hash(s):
    return int(sha512(str(s)).hexdigest(), 16)


p = 285370232948523998980902649176998223002378361587332218493775786752826166161423082436982297888443231240619463576886971476889906175870272573060319231258784649665194518832695848032181036303102119334432612172767710672560390596241136280678425624046988433310588364872005613290545811367950034187020564546262381876467

pwds = []
for k in range(11):
    for pwd in range(1, 17):
        print pwd
        s1, f1 = sock(remoteip, remoteport)
        s2, f2 = sock(remoteip, remoteport)
        for i in range(11):
            if i != k:
                bb1 = get_bb(f1)
                bb2 = get_bb(f2)

                s1.send(str(bb2)+"\n")
                s2.send(str(bb1)+"\n")
            else:

                num1 = get_hash(get_bb(f1))
                num2 = get_hash(get_bb(f2))

                aa = pow(get_hash(pwd), 2, p)

                assert aa > 514 and aa <= p - 514
                s1.send(str(aa)+"\n")
                s2.send(str(aa)+"\n")

        enc1 = get_enc(f1)
        enc2 = get_enc(f2)
        if enc1^num1 == enc2^num2:
            print "[+] pwd %d: %d" % (k, pwd)
            pwds.append(pwd)
            break

        s1.close()
        s2.close()


s, f = sock(remoteip, remoteport)
bbs = []
key = 0

for pwd in pwds:
    key ^= get_hash(get_bb(f))
    aa = pow(get_hash(pwd), 2, p)
    s.send(str(aa)+"\n")

enc = get_enc(f)
print long_to_bytes(enc ^ key)
s.close()
