from Crypto.Cipher import AES
import base64
import os
import sys
import getpass

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: str(c.decrypt(base64.b64decode(e)), 'utf-8').rstrip(PADDING)

# generate a random secret key
secret = "your_secret_key".encode()

# create a cipher object using the random secret
cipher = AES.new(secret)

#Prompt text input on CLI for encryption
p = getpass.getpass("Insert password:")

#Print out encrypted passcode
encoded = EncodeAES(cipher, p)
print('Encrypted string:', encoded)

#Use to decode encrypted passcode
#decoded = DecodeAES(cipher, b'XV0gmroQ71QPkLln+5boow==')
#print('Decrypted string:', decoded)
