import socket
import subprocess
import ctypes
import struct
import os

remoteip   = "katagaitai.orz.hm"
remoteport = 4321

dll = ctypes.cdll.LoadLibrary("./my_hash_extender.so")

def sock(remoteip, remoteport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip, remoteport))
    return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
    data = ''
    while not data.endswith(delim):
        data += f.read(1)
    return data


def length_extension(x, y, test_hash):
    cmd = 'hash_extender -d %s -a %s -s %s -l 16 -f md5' % (x, y, test_hash)
    ret  =  subprocess.check_output(cmd.split(" "))
    lines = ret.split("\n")
    signature = lines[2].split(" ")[-1]
    string = lines[3].split(" ")[-1].decode("hex")
    return signature, string

s, f = sock(remoteip, remoteport)
print read_until(f, "quit")
s.send("1\n")
read_until(f, "100):")
s.send("100\n")
read_until(f, "quit")
s.send("3\n")
read_until(f, "round")
s.send("a")
read_until(f, "generated ")
suffix = int(read_until(f, ",")[:-1])
suffix = hex(suffix)[2:].strip("L").rjust(32, '0')
print "[+] suffix:", suffix

related_hash, related_str = length_extension('a', 'b', suffix)

s.send("3\n")
read_until(f, "round")
s.send(related_str)
read_until(f, "generated ")
related_suffix = int(read_until(f, ",")[:-1])
related_suffix = hex(related_suffix)[2:].strip("L").rjust(32, '0')
print "[+] related_suffix: ", related_suffix

A, B, C, D = struct.unpack(">4I", suffix.decode("hex"))
A = dll.brute(A, B, C, D, related_suffix)
full_hash = struct.pack(">4I", A, B, C, D).encode("hex")
print "[+] full_hash", full_hash

balance = 1000

while True:
    add = os.urandom(8).encode("hex")
    new_hash, new_str = length_extension('a', add, full_hash)
    n = int(new_hash, 16)

    odds = 0
    while n % 2 == 0:
        odds += 1
        n >>= 1

    if odds == 0:
        continue

    print read_until(f, "quit")
    s.send("1\n")
    print read_until(f, "100):")
    s.send(str(odds)+ "\n")

    print read_until(f, "quit")
    s.send("2\n")
    print read_until(f, "):")
    s.send(str(balance)+ "\n")

    print read_until(f, "quit")
    s.send("3\n")
    print read_until(f, "round")
    s.send(new_str)

    balance += odds * balance

s.close()
