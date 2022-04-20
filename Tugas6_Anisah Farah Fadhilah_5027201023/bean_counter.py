import requests, io
from PIL import Image
from pwn import xor

URL = "http://aes.cryptohack.org/bean_counter/encrypt"
PNG_PREFIX = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

r = requests.get(url=URL)
enc_bytes = bytes.fromhex(r.json()['encrypted'])

keystream = xor(PNG_PREFIX, enc_bytes[:16])

pt = xor(enc_bytes, keystream)

image = Image.open(io.BytesIO(pt))
image.save('flag.png')