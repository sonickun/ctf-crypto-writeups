def plus(x, y):
    return (x + y) & 0xffffffff

def rotate(x, n):
    y = x << n
    z = x >> (32 - n)
    return (y | z) & 0xffffffff

def make_array(s):
    v = [s[i: i+2] for i in range(0, len(s), 2)]
    return map(lambda x : int(x,16), v)

def quaterround(a, b, c, d):
    a = plus(a, b)
    d ^= a
    d = rotate(d, 16)

    c = plus(c, d)
    b ^= c
    b = rotate(b, 12)

    a = plus(a, b)
    d ^= a
    d = rotate(d, 8)

    c = plus(c, d)
    b ^= c
    b = rotate(b, 7)

    return a, b, c, d


def chacha(k, n, cipher):
    #=====initial state=====
    sigma = [
        101, 120, 112, 97,
        110, 100, 32, 51,
        50, 45, 98, 121,
        116, 101, 32, 107
    ]
    key = make_array(k) 
    block_count = [0, 0, 0, 0, 0, 0, 0, 0]
    nonce = make_array(n)

    in1 = sigma + key + block_count + nonce

    #=====littleendian=====
    x = []
    for i in range(0, len(in1), 4):
        x.append(in1[i] + (in1[i+1] << 8) + (in1[i+2] << 16) + (in1[i+3] << 24))

    #=====main function=====
    cp = list(x)
    for i in range(10):
        # column rounds
        x[0], x[4], x[8], x[12] = quaterround(x[0], x[4], x[8], x[12])
        x[1], x[5], x[9], x[13] = quaterround(x[1], x[5], x[9], x[13])
        x[2], x[6], x[10], x[14] = quaterround(x[2], x[6], x[10], x[14])
        x[3], x[7], x[11], x[15] = quaterround(x[3], x[7], x[11], x[15])
        # diagonal rounds
        x[0], x[5], x[10], x[15] = quaterround(x[0], x[5], x[10], x[15])
        x[1], x[6], x[11], x[12] = quaterround(x[1], x[6], x[11], x[12])
        x[2], x[7], x[8], x[13] = quaterround(x[2], x[7], x[8], x[13])
        x[3], x[4], x[9], x[14] = quaterround(x[3], x[4], x[9], x[14])

    for i in range(16):
        x[i] = plus(x[i], cp[i])

    #=====littleendian inverse=====
    result = []
    for i in range(len(x)):
        result.append(x[i] & 0xff)
        result.append((x[i] >> 8) & 0xff)
        result.append((x[i] >> 16) & 0xff)
        result.append((x[i] >> 24) & 0xff)

    #=====encryption/decryption=====
    c = []
    m = make_array(cipher)
    for i in range(len(m)):
        c.append(result[i] ^ m[i])

    print 'flag:', "".join(map(lambda x : chr(x), c))


if __name__ == '__main__':

    key = "23AD52B15FA7EBDC4672D72289253D95DC9A4324FC369F593FDCC7733AD77617"
    nonce = "5A5F6C13C1F12653"
    cipher = "6bd00ba222523f58de196fb471eea08d9fff95b5bbe6123dd3a8b9026ac0fa84"

    chacha(key, nonce, cipher)
