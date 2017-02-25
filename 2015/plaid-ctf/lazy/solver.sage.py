# filename: solver.sage

from Crypto.Util.number import long_to_bytes as l2b

def create_matrix(pub, c):
    n = len(pub)
    i = matrix.identity(n) * 2
    last_col = [-1] * n
    first_row = []
    for p in pub:
        first_row.append(int(long(p)))
    first_row.append(-c)

    m = matrix(ZZ, 1, n+1, first_row)
    bottom = i.augment(matrix(ZZ, n, 1, last_col))
    m = m.stack(bottom)
    return m


def is_target_value(V):
    for v in V:
        if v!=-1 and v!=1:
            return False
    return True


def find_shortest_vector(matrix):
    for col in matrix.columns():
        if col[0] == 0 and is_target_value(col[1:]):
            return col
        else:
            continue


pub = eval(open("pubkey.txt", "r").read())
c = int(open("ciphertext.txt", "r").read())

m = create_matrix(pub, c)
lllm = m.transpose().LLL().transpose()

shortest_vector = find_shortest_vector(lllm)

print shortest_vector

x = ""
for v in shortest_vector[1:]:
    if v == 1:
        x += "1"
    elif v == -1:
        x += "0"

flag = l2b(int(x[::-1], 2))

print flag

# lenstra_and_lovasz_liked_lattices

