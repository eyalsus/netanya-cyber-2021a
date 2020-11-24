from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

message = b'hello world!!!!!hello world!!!!!'
key = get_random_bytes(16)

ciphers = {
    'ECB': AES.new(key, AES.MODE_ECB),
    'CTR': AES.new(key, AES.MODE_CTR),
    'CBC': AES.new(key, AES.MODE_CBC)
}

for name, cipher in ciphers.items(): 
    print(name)
    for _ in range(5):
        c = cipher.encrypt(message)
        print(c) 
