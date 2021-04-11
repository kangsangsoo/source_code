import requests, json


URL = "http://aes.cryptohack.org/ctrime/encrypt/"



# "crypto{CRIM 에서 끊어지기 때문에 아무거나 가정하고 돌려보면 됨. => E
plaintext = "crypto{"

for i in range(20):
    min_num = 200
    min_ch = 0
    for j in range(39, 127):
        
        inp = plaintext + chr(j)
        
        length = len(requests.get(URL + inp.encode().hex()).json()["ciphertext"])

        print(chr(j) + ": " + str(length))
        if length < min_num:
            min_ch = j
            min_num = length
        
    plaintext = plaintext + chr(min_ch)
    print(plaintext)
