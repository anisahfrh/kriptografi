import requests
from Crypto.Cipher import AES
from hashlib import md5

url = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
words = requests.get(url).text.splitlines()
cypher = bytes.fromhex("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66")

for key in words:
    key = md5(key.encode()).digest()
    aes = AES.new(key, AES.MODE_ECB)
    doc = aes.decrypt(cypher)
    if b'crypto' in doc:
        print(doc)