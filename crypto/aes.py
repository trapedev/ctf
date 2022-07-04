from re import A
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'16bytes_key12345'
message = b'helloworld'
cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(pad(message, 16))
dec = unpad(cipher.decrypt(enc), 16)
print(enc)
print(dec)