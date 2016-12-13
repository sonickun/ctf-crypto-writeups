def calc_hash(key):
	h = 0x539 
	target = 0xEF2E3558
	for k in key:
		h += (h<<5) + ord(k)
		h &= 0xFFFFFFFF
	return abs(target - h)

charset = [chr(i) for i in range(0x21,0x7e)]

key = ""
MAX_LEN = 10

while True:
	min_diff = 0xFFFFFFFF
	min_chr = None
	tmp_key = key
	for c in charset:
		for i in range(1, MAX_LEN-len(key)):
			test = tmp_key + (c * i)
			# print test
			diff = calc_hash(test)
			if diff < min_diff:
				min_diff = diff
				min_chr = c
	key = tmp_key + min_chr
	print "min_diff: %d, key: %s" % (min_diff, key)
	if min_diff == 0:
		print "Gotcha!:", key
		break

	if len(key) == MAX_LEN:
		print "key not found :("
		break
