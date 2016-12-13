# -*- coding: utf-8 -*- 
import socket
import time

def egcd(a, b):
	(x, lastx) = (0, 1)
	(y, lasty) = (1, 0)
	while b != 0:
		q = a // b
		(a, b) = (b, a % b)
		(x, lastx) = (lastx - q * x, x)
		(y, lasty) = (lasty - q * y, y)
	return (lastx, lasty, a)

def modinv(a, m):
	(inv, q, gcd_val) = egcd(a, m)
	return inv % m

def calc(n,c1,c2):
	m = (c2 + 2*c1 - 1) * modinv(c2 - c1 + 2, n) % n
	return m

def first(clientsock):
	line1 = clientsock.recv(1024)
	line2 = clientsock.recv(1024)
	n, c1 = map(int,line1.split("\n"))
	c2 = int(line2.strip())
	m = calc(n,c1,c2)
	print "m=",m
	clientsock.sendall(str(m)+"\n")
	time.sleep(0.5)


def mid(clientsock):
	line = clientsock.recv(1024)
	print line
	n ,c1,c2 = map(int, line.split("\n")[1:4])
	m = calc(n,c1,c2)
	print "m=",m
	clientsock.sendall(str(m)+"\n")
	time.sleep(0.5)


def last(clientsock):
	line = clientsock.recv(1024)
	print line
	n ,c1,c2 = map(int, line.split("\n")[1:4])
	m = calc(n,c1,c2)
	print "m=",m
	print 
	print "flag:", hex(m)[2:-1].decode('hex')

host = 'localhost'
port = 8888

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((host,port))

first(clientsock)

for i in range(1,9):
	print i
 	mid(clientsock)

last(clientsock)

clientsock.close() 
