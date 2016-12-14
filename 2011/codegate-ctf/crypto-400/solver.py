# CODEGATE2011 Crypto 400

import base64

f = open("2404656D5DA22F5DBA41CDD7AA1C1F7B", "r")

array = []
for line in f:
	status = line.strip().split(" ")[-1]
	a = line.split(" ")[9].replace("/","")
	data = base64.urlsafe_b64decode(a+"=").encode("hex")
	# print data
	one = data[:32]
	two = data[32:]
	if status != "500":
		 array.append([one, two])
	# print len(data)

f.close()

one = int(array[-1][0], 16)

padd = int("10101010101010101010101010101010", 16)

decipher = one ^ padd

first = int(array[0][0], 16)

plaintext = hex(decipher ^ first)[2:-1].decode("hex")
print plaintext