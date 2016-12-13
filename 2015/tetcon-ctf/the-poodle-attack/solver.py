import urllib2
import sys
import copy

BLOCK_SIZE = 16

def chunks(l, n):
    if n < 1:
        n = 1
    return [l[i:i + n] for i in range(0, len(l), n)]


def httpcode(url):
    try:
        req = urllib2.Request(url)
        f = urllib2.urlopen(req)
        return f.getcode()
    except urllib2.HTTPError, e:
        return e.code

def http(url):
    try:
        req = urllib2.Request(url)
        f = urllib2.urlopen(req)
        return f.read()
    except urllib2.HTTPError, e:
        return e.code


FLAG = ""

for m in range(1,3):
    for n in range(1, BLOCK_SIZE+1):
        url = 'http://crypto-class.appspot.com/tetcon?p1=AAAAAAAAAAAAAAAA%s&p2=AAAAAAAAAAAAAAAA%s' % ('B'*(BLOCK_SIZE-n),'B'*n)
        cipher_block = chunks(http(url).strip(),32)
        xor_byte = int("0x"+cipher_block[m][-2:], 16)
        for i in range(256):
            new_block = copy.copy(cipher_block)
            new_block.append(new_block[m+1])
            new_block[len(cipher_block)-1] = 'ff'*15+hex(i)[2:].zfill(2)
            url = 'http://crypto-class.appspot.com/tetcon?c=%s' % ''.join(new_block)
            rescode = httpcode(url)
            if rescode != 403:
                print i
                c = 31 ^ i ^ xor_byte
                FLAG += chr(c)
                print '==>',chr(c),FLAG
                break

print 'Flag:',FLAG
