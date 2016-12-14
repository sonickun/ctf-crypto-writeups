#flag begins with h4ck1t{

def slice(s, size):
    return [s[i: i+size] for i in range(0, len(s), size)]

def xor(a, b):
    return "".join([chr(ord(a[i]) ^ ord(b[i % len(b)])) for i in xrange(len(a))])

def f(L, n):
    ans = ""
    for i in range(len(L)):
        ans += chr((ord(L[i]) + n) % 256)
    return ans

def ninja_decrypt(cipher, rounds):
    assert len(cipher) == 8
    right = cipher[4:]
    left = cipher[:4]

    tmp = left
    left = right
    right = tmp

    for n in reversed(range(1, rounds+1)):
        tmp = left
        left = right
        right = xor(tmp, f(right, n))

    return left + right


cipher = "dd67ca82d358f0c8479e118addcec2f8ce086c0f6f239f9b66d7226a38c68198dbd777f366fb9fd83b60d11109be174759c75ea56a4866c2"

cipher = slice(cipher.decode("hex"), 8)

# print map(lambda x: x.encode("hex"), cipher)

for i in range(1000):
    plain = ninja_decrypt(cipher[0], i)
    if plain.find("h4ck1t{") >= 0:
        print "found", i
        rounds = i

flag = ""
for c in cipher:
    flag += ninja_decrypt(c, rounds)

print flag
# h4ck1t{KV_F315T31_Kn0VVS_H1S_NN3Tvv0Rk_PrEttY_a1nt_B4D}
