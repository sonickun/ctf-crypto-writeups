a = 1234577
b = 3213242
M = 7654319


def add(A,B):
    if A==(0,0): return B
    if B==(0,0): return A
    x1,y1 = A
    x2,y2 = B
    if A!=B:
        p = (y2-y1)*pow(x2-x1,M-2,M)
    else:
        p = (3*x1*x1+a)*pow(2*y1,M-2,M)
    x3 = p*p-x1-x2
    y3 = p*(x1-x3)-y1
    return (x3%M,y3%M)

base = (5234568, 2287747)
pub = (2366653, 1424308)

crypt =  [(5081741, 6744615), (610619, 6218)]


X = (0,0)

for i in range(M):
    if X==pub:
        secret = i
        print "secret:" + str(secret)
        break
    X = add(X, base)
    print i

#secret  = 1584718

tmp =(0,0)

for i in range(1584718):
    tmp = add(tmp,crypt[0])

plain = add(crypt[1], (tmp[0],tmp[1]*-1))

print plain

# 2171002 + 3549912 = 5720914
