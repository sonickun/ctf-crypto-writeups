import socket
from Crypto.Util.number import bytes_to_long, long_to_bytes

remoteip   = "trumptrump.pwn.republican"
remoteport = 3609

def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data


e = 65537
N = 23377710160585068929761618506991996226542827370307182169629858568023543788780175313008507293451307895240053109844393208095341963888750810795999334637219913785780317641204067199776554612826093939173529500677723999107174626333341127815073405082534438012567142969114708624398382362018792541727467478404573610869661887188854467262618007499261337953423761782551432338613283104868149867800953840280656722019640237553189669977426208944252707288724850642450845754249981895191279748269118285047312864220756292406661460782844868432184013840652299561380626402855579897282032613371294445650368096906572685254142278651577097577263

picture = open("trump.jpg", "rb").read()
picture_long = bytes_to_long(picture)
m = picture_long % N

assert m % 5 == 0

s, f = sock(remoteip, remoteport)
read_until(f, ">")
s.send(str(m/5) + "\r\n")
read_until(f, "kid: ")
s1 = int(read_until(f, "\n").strip())
print "[+] s1:", s1
s.close()

s, f = sock(remoteip, remoteport)
read_until(f, ">")
s.send(str(5) + "\r\n")
read_until(f, "kid: ")
s2 = int(read_until(f, "\n").strip())
print "[+] s2:", s2
s.close()

sig = (s1 * s2) % N
print "[+] Signature:", sig

s, f = sock(remoteip, remoteport)
read_until(f, ">")
s.send(str(sig) + "\r\n")
read_until(f, "it.\n")
payload = int(read_until(f, "\n").strip(), 16)
f.close()


open("flag.jpg", "wb").write(long_to_bytes(payload))
print "Picture saved."
