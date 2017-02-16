import requests
import string

url = "https://cthulhu.fluxfingers.net:1505/"

flag = "M"
flag = "Mu7a"
while True:
    payload = {'user': flag+":"}
    r = requests.get(url, params=payload)
    base = len(r.cookies['auth'].decode("base64"))
    print "base", base
    for c in string.printable:

        payload = {'user': flag+c}

        r = requests.get(url, params=payload)

        print r.text
        authLen = len(r.cookies['auth'].decode("base64"))
        print authLen
        if authLen < base:
            flag += c
            break


print "flag:", flag[:-1]

