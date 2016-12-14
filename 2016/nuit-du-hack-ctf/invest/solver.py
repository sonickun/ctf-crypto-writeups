import  base64
import struct

def calc_not(a):
	if a == 1:
		return 0
	else:
		return 1

def make_stream(k):
	key = map(int, k)
	# print key
	a0 = key[0] & calc_not(key[2])
	a1 = calc_not(key[3])
	a2 = calc_not(key[4])
	a3 = calc_not(key[2]) & calc_not(key[1])
	a4 = key[0] & key[1]
	a5 = calc_not(key[5])
	a6 = key[2]
	a7 = key[5] ^ key[6]
	a8 = calc_not(key[7]) ^ calc_not(key[1])
	# print a0,a1,a2,a3,a4,a5,a6,a7,a8
	b0 = a0 & a1
	b1 = a2
	b2 = a1 & a3
	b3 = a1 & a4
	b4 = a5 & a6
	b5 = a7
	b6 = a6 & a8

	c0 = b0 & b1
	c1 = b1 & b2
	c2 = b1 & b3
	c3 = b4 & b5
	c4 = b6

	d0 = c0 | c1
	d1 = c2 | c3
	d2 = c4

	out = d0 | (d1 | d2)

	return str(out)


key = "010001110101111001100011011011100100100100111001010111100100011101000111001110010100011100111001010001110011100101000111001110010101111001100011011011100100100101101110010010010011100100110101010111100110001100111001001101010110111001001001011011100100100101000111010111100011100100110101011011100100100101011110011000110100011101011110001110010011010101011110011000110101111001100011010111100110001101000111010111100101111001100011011011100100100101000111010111100011100100110101010001110101111001101110010010010101111001100011010111100110001101101110010010010101111001100011010111100110001100111001001101010100011101011110010111100110001101011110011000110101111001100011010001110101111001000111010111100101111001100011011011100100100101101110010010010101111001100011"
divided_key = [key[i: i+8] for i in range(0, len(key), 8)]

stream = ""
for d in divided_key:
	stream += make_stream(d)

stream = int(stream, 2)

print "password:",hex(stream)[2:-1].decode("hex")
# exit()
# print len(stream)

# f = open("encrypt","r")
# encrypt = f.read()
# f.close()

# data = base64.b64decode(encrypt).encode("hex")
# divided_data = [data[i: i+24] for i in range(0, len(data), 24)]


# key =int(key, 2)
# data = int(data[:192], 16)

# print hex(key)
# print hex(data)

# plain = key ^ data
# plain = hex(plain)[2:-1]
# print plain
# plain = ""
# for d in divided_data:
# 	p = stream ^ int(d, 16)
# 	try:
		
		# print bin(stream)
		# print bin(int(d, 16))
		# print bin(plain)
		# print hex(plain)[2:-1]
	# 	plain += hex(p)[2:-1]

	# except:
	# 	print "except"
	# 	print hex(plain)
	# 	break

# print plain

# divided_data = [plain[i: i+2] for i in range(0, len(plain), 2)]
# print divided_data

# f = open("outfile","wb")
# for d in divided_data:
# 	f.write(struct.pack("B",int(d, 16)))
# f.close()



# key =int(key, 2)
# data = int(data[:192], 16)

# print hex(key)
# print hex(data)

# plain = key ^ data
# print hex(plain)[2:-1].decode("hex")