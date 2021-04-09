import requests, json
from Crypto.Util.number import long_to_bytes, bytes_to_long


URL = "http://aes.cryptohack.org/flipping_cookie/"

s = bytes_to_long(b"admin=False;expi") ^ bytes_to_long(b"admin=True;expir")

res = requests.get(URL + "get_cookie/").json()["cookie"]

iv = res[:32]
c = res[32:]

iv_ = int(iv, 16) ^ s
iv_ = hex(iv_)[2:]
print(res)
print(iv_)

res = requests.get(URL + "check_admin/" + c + "/" + iv_)

print(res.text)
