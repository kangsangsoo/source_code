import requests, json
from Crypto.Util.number import long_to_bytes, bytes_to_long


URL = "http://aes.cryptohack.org/bean_counter/encrypt"

res = requests.get(URL).json()["encrypted"]


key = "55cce30e8f5e0322f6da7e4f161b49c7"
data = ""

for i in range(0, len(res), 2):
    g = hex((int(key[i%32]+key[(i+1)%32],16) ^ int(res[i] + res[i+1], 16)))[2:]
    if len(g) == 1:
        g = '0' + g
    data = data + g

print(data)

with open("./test.png", "wb") as f:
    f.write(long_to_bytes(int(data, 16)))
