print("Rvksu")

from Crypto.Cipher import AES
import zlib

filename = "downloadconfigfile.conf"
output = "output.xml"

key = bytes([26,170,180,167,48,178,62,31,200,161,213,156,121,40,58,34,
             139,120,65,14,204,70,250,79,72,235,20,86,226,76,91,137])
iv = bytes([209,254,117,18,50,92,87,19,211,98,211,50,175,163,100,76])

with open(filename, "rb") as f:
    file_content = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(file_content)

print(decrypted[:16].hex())

try:
    decompressed = zlib.decompress(decrypted[2:], -15)
except Exception as e:
    print(e)
    exit(1)

cleaned = decompressed[:-129]

with open(output, "wb") as f:
    f.write(cleaned)

print("Configuration successfully decrypted")
