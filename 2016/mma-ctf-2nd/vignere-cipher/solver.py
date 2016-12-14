import collections
import itertools
from base64 import b64encode, b64decode

def shift(char, key, rev = False):
    if not char in chars:
        return char
    if rev:
        return chars[(chars.index(char) - chars.index(key)) % len(chars)]
    else:
        return chars[(chars.index(char) + chars.index(key)) % len(chars)]

def decrypt(encrypted, key):
	try:
		encrypted = ''.join([shift(encrypted[i], key[i % len(key)], True) for i in range(len(encrypted))])
		return b64decode(encrypted.encode('ascii')).decode('ascii')
	except:
		return ''

def is_valid(encrypted, pre_key, block):
	key = add_pad(pre_key, key_len)
	encrypted = ''.join([shift(encrypted[i], key[i % len(key)], True) for i in range(len(encrypted))])
	if len(pre_key) % 4 == 2:
		for i in range(0, len(b64decode(encrypted.encode('ascii')))-6, 9):
			if check_ascii([b64decode(encrypted.encode('ascii'))[i+(block*3)]]) == False:
				return False
		return True
	else:
		for i in range(0, len(b64decode(encrypted.encode('ascii')))-6, 9):
			if check_ascii(b64decode(encrypted.encode('ascii'))[i+(block*3):i+(block*3)+len(pre_key)-(block*4)-1]) == False:
				return False
		return True


def add_pad(key, key_len):
	return key + "a"*(key_len - len(key))

def check_ascii(text):
	for t in text:
		if (t == 10) or (t > 31 and t < 127):
			pass
		else:
			return False
	return True

cipher = open("encrypted.txt", "r").read().strip()

list = []

# Kasiski-Test
for i in range(len(cipher)-2):
	list.append(cipher[i:i+3])

# print(collections.Counter(list))
# {'Z96': 2, 'Tl0': 2, 'Aw1': 2, 'eCa': 2, '4vN': 2, 'ZT6': 2, 'BDz': 2, 'DzX': 2, 'eAw': 2 }

overlap = {'Z96', 'Tl0', 'Aw1', 'eCa', '4vN', 'ZT6', 'BDz', 'DzX', 'eAw'}

for s in overlap:
	a = [-1, -1]
	for i in range(len(cipher)-2):
		if cipher[i:i+3] == s:
			if a[0] == -1:
				a[0] = i
			else:
				a[1] = i
				break
	print("%s: %d" % (s, a[1] - a[0]))

# Tl0: 144
# BDz: 156
# 4vN: 204
# eAw: 192
# eCa: 60
# DzX: 156
# Z96: 96
# Aw1: 192
# ZT6: 60

# common divisor
# 1, 2, 3, 4, 6, 12

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'

key_len = 12

keylist= [[],[],[]]

for block in range(3):
	for k in itertools.product(chars, repeat=2):
		pre_key0 = "a"*(4*block) + ''.join(k)
		if is_valid(cipher, pre_key0, block) == False:
			continue
		for x in chars:
			pre_key1 = pre_key0 + x
			if is_valid(cipher, pre_key1, block) == False:
				continue
			for y in chars:
				pre_key2 = pre_key1 + y
				if is_valid(cipher, pre_key2, block) == False:
					continue
				print ("[+] Block%d: %s" % (block, pre_key2[4*block:4*(block+1)]))
				keylist[block].append(pre_key2[4*block:4*(block+1)])
	print()

print ("Searching...")
for k1 in keylist[0]:
	for k2 in keylist[1]:
		for k3 in keylist[2]:
			fullkey = k1 + k2 + k3
			plain = decrypt(cipher, fullkey)
			if plain.find("TWCTF{") >= 0:
				print("[+] Found! key:", fullkey)
				print(plain)
				break


# [+] Found! key: shA6I8HUXLFY
# SKK is a Japanese Input Method developed by Sato Masahiko. Original SKK targets Emacs. However, there are various SKK programs that works other systems such as SKKFEP(for Windows), AquaSKK(for MacOS X) and eskk(for vim).
# OK, the flag is TWCTF{C14ss1caL CiPhEr iS v3ry fun}.