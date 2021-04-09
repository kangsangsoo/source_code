import requests, json
from Crypto.Util.number import long_to_bytes



URL = "http://aes.cryptohack.org/ecbcbcwtf/"

c = requests.get(URL + "encrypt_flag").json()["ciphertext"]
iv = c[:32]

flag = ""

for i in range(1,3):
    c_ = c[32*i:32*(i+1)]

    p_ = requests.get(URL + "decrypt/" + c_).json()["plaintext"]

    res = hex(int(p_,16) ^ int(iv, 16))[2:]

    flag = flag + res 
    iv = c_

print(long_to_bytes(int(flag, 16)))
