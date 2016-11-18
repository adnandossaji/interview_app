import os
from Crypto.Util.number import getPrime
from encrypt import Encrypt
from test2 import DiffieHellman
import hashlib
from binascii import hexlify # For debug output

a = DiffieHellman()
b = DiffieHellman()

key = a.genKey(b.publicKey)
key2 = b.genKey(a.publicKey)

enc = Encrypt(key)
message = "Hey!"
message = enc.encrypt(message)
message = enc.decrypt(message)
print(message)
