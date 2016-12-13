import itertools

cipher = '805eed80cbbccb94c36413275780ec94a857dfec8da8ca94a8c313a8ccf9'

for i, j in itertools.product(range(251), repeat=2):
    if (ord("T")*i+j)%251==0x80 and (ord("W")*i+j)%251==0x5e:          
        a, b = i, j
        break   

print a, b

flag = ''
for i in range(0, len(cipher), 2):
    m = int(cipher[i:i+2], 16)
    for i in range(0x20,0x7f):
       if (i*a+b)%251 == m:
        flag += chr(i)

print flag

# flag: TWCTF{Faster_Than_Shinkansen!}