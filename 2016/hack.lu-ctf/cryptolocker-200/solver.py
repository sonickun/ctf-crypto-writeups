import sys
import hashlib
from AESCipher import *
import string
import itertools

class SecureEncryption(object):
    def __init__(self, keys):
        #assert len(keys) == 4
        self.keys = keys
        self.ciphers = []
        for i in range(len(keys)):
            self.ciphers.append(AESCipher(keys[i]))

    def enc(self, plaintext): # Because one encryption is not secure enough
        one        = self.ciphers[0].encrypt(plaintext)
        two        = self.ciphers[1].encrypt(one)
        three      = self.ciphers[2].encrypt(two)
        ciphertext = self.ciphers[3].encrypt(three)
        return ciphertext

    def dec(self, ciphertext):
        three      = AESCipher._unpad(self.ciphers[3].decrypt(ciphertext))
        two        = AESCipher._unpad(self.ciphers[2].decrypt(three))
        one        = AESCipher._unpad(self.ciphers[1].decrypt(two))
        plaintext  = AESCipher._unpad(self.ciphers[0].decrypt(one))
        return plaintext

    def mydec(self, ciphertext):
        tmp = ciphertext
        for i in range(len(self.keys)-1):
            tmp = AESCipher._unpad(self.ciphers[len(self.keys)-i-1].decrypt(tmp))
        plaintext = self.ciphers[0].decrypt(tmp)
        return plaintext


def checkPadding1(plain):
    padlen = ord(plain[-1])
    pad = chr(padlen)*padlen
    if plain[-padlen:] != pad or padlen > 32 or padlen == 1:
        return False
    else:
        return True

def checkPadding2(plain):
    pad = chr(16)*16
    if len(plain) > 1 and plain[-16:] == pad:
        return True
    else:
        return False

cipher = open("flag.encrypted", "rb").read()

keys = []
password = ""
charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(4):
    for c in itertools.product(charset, repeat=2):
        user_input = "".join(c)
        tmp_keys = keys[:]
        tmp_keys.insert(0, hashlib.sha256(user_input).digest())
        s = SecureEncryption(tmp_keys)
        plain = s.mydec(cipher)

        if i == 3:
            if checkPadding1(plain):
                keys = tmp_keys[:]
                password = user_input + password
                print "[+] found password:", password
                open("flag.odt", "wb").write(AESCipher._unpad(plain))
                break
        else:
            if checkPadding2(plain):
                keys = tmp_keys[:]
                password = user_input + password
                print "[+] found password:", password
                break

#[+] found password: Sg52WH4D
# Flag: flag{v3ry_b4d_crypt0_l0ck3r}
