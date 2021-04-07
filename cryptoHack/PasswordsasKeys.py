import requests, json, hashlib
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Cipher import AES

URL = 'http://aes.cryptohack.org/passwords_as_keys/encrypt_flag'
response = requests.get(URL)
c = bytes.fromhex(response.json()["ciphertext"])

print(c)

with open("./words.txt") as f:
    words = [w.strip() for w in f.readlines()]

print(len(words))
for i in words:
    KEY = hashlib.md5(i.encode()).digest()
    cipher = AES.new(KEY, AES.MODE_ECB)
    m = cipher.decrypt(c)
    print(m)
    if m[0:3] == b"cry":
        print(m)
        break
