import socket
from hashlib import md5
import telnetlib

remoteip   = "localhost"
remoteport = 54321
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 

def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data

def shell(s):
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()


def main():
    s, f = sock(remoteip, remoteport)
    print read_until(f, "ogin\n"),
    s.send("r\n")

    # Data = md5("admin"+pad) + ("admin"+pad)
    data = pad("admin")
    data = md5(data).digest() + data
    print data.encode("hex")
    s.send(data + "\n")

    print read_until(f),
    secret = read_until(f).strip()
    # Remove the first 16 bytes
    secret = secret[BS*2:]

    print read_until(f, "ogin\n"),
    s.send("l\n")
    s.send(secret + "\n")
    print secret

    shell(s)
    s.close()

if __name__ == '__main__':
    main()
