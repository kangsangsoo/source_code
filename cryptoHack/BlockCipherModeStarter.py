import requests, json
from Crypto.Util.number import long_to_bytes

URL = 'http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/'
response = requests.get(URL)
c = response.json()["ciphertext"]

print(c)
URL = 'http://aes.cryptohack.org/block_cipher_starter/decrypt/' + c 
response = requests.get(URL)
m = response.json()["plaintext"]

print(long_to_bytes(int(m, 16)))
