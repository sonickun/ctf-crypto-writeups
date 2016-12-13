import requests

def make_blocks(s):
   	return [s[i:i+16] for i in xrange(0, len(s), 16)]

def xor(a, b):
	return "".join([chr(ord(a[i]) ^ ord(b[i % len(b)])) for i in xrange(len(a))])
 
def decrypt(target):
	prefix = "578ae51334b467aa99092c00e57ff977168f922a.4f3a3680afa88ae056e5c56fb67544ff03e5b64f4174f1752ab93ac24a78257fc173ab2f339436453e9163265fd23707"
	url = "https://wolf-spider.ctfcompetition.com/admin"
	target = target.encode("hex")
	after_enc = ""
	for k in range(16):
		s = ""
		for i in xrange(k):
			c = after_enc[::-1][i]
			n = ord(c) ^ (k + 1)
			s = "%02x%s" % (n, s)

		for i in xrange(0,256):
			print
			print "i:%d after_enc:%s" % (i, after_enc.encode("hex"))
			mid = "%02x%s" % (i, s)
			mid = mid.rjust(32, "0")
			uid = prefix + mid + target
			res = requests.get(url, verify=False, cookies={"UID": uid})
			rescode = res.status_code
			if rescode != 500:
				after_enc = chr(i ^ (k + 1)) + after_enc
				print after_enc.encode("hex")
				break
			
	return after_enc

def main():
	# username=hoge\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01h&username=admin
	sig = "757365726e616d653d686f67658000000000000000000000000000000000016826757365726e616d653d61646d696e01"
	sig_hash = "b78ca576701807fc18e64db090aa4f6939232416"

	target_block = make_blocks(sig.decode("hex"))
	target_block.reverse()

	# login as "aaaaaaa"
	# 578ae51334b467aa99092c00e57ff977168f922a.4f3a3680afa88ae056e5c56fb67544ff03e5b64f4174f1752ab93ac24a78257fc173ab2f339436453e9163265fd23707
	ct = "4f3a3680afa88ae056e5c56fb67544ff03e5b64f4174f1752ab93ac24a78257fc173ab2f339436453e9163265fd23707".decode("hex")
	IV = ct[:16]
	ciphertext = ct[16:32]
	ciphertext = xor(xor(IV, "username=aaaaaaa"), target_block[0]) + ciphertext

	for i in range(1,3):
		after_enc = decrypt(ciphertext[:16])
		ciphertext = xor(after_enc, target_block[i]) + ciphertext

	uid = "%s.%s" % (sig_hash, ciphertext.encode("hex"))
	print "UID:", uid

if __name__ == '__main__':
	main()
	
# Result
# UID: b78ca576701807fc18e64db090aa4f6939232416.dc3cd1cc0697b720cd117bb4f59b7b71ccb94738c7f771ba5af213666f00f9a21c3c2097b3a786e80eb9c56aba7d4b9f03e5b64f4174f1752ab93ac24a78257f
