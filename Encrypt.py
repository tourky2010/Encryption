#!/usr/bin/python
__author__ = 'Tourky'

# need pycrypto package
#from Cryptodome.Cipher import AES
#from Cryptodome.Hash import SHA256
import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# key has to be 16, 24 or 32 bytes long
result = b''
def key_gen():
    key=input('Enter the Key: ' )
    hash_obj = SHA256.new(key.encode('utf-8'))
    hash_key = hash_obj.digest()
    return hash_key

def tourky_encrypt_ECB(plain):
    msg=plain
    block_size = 16
    pad = "{"
    padding = lambda s: s + (block_size - len(s) % block_size) * pad
    print('AES ECB chosen\n')
    key=key_gen()
    cipher = AES.new(key, AES.MODE_ECB)
    result = cipher.encrypt(padding(msg).encode('utf-8'))
    return result

def tourky_encrypt_CBC(plain):
    msg=plain
    block_size = 16
    pad = "{"
    iv='Hmada is awsomee'
    padding = lambda s: s + (block_size - len(s) % block_size) * pad
    print('AES CBC chosen\n')
    key=key_gen()
    cipher = AES.new(key, AES.MODE_CBC, iv.encode('utf-8'))
    global result
    result = cipher.encrypt(padding(msg).encode('utf-8'))
    return result

def tourky_decrypt_ECB(cipher):
    msg=cipher
    pad='{'
    key=key_gen()
    decipher= AES.new(key, AES.MODE_ECB)
    plain_test = decipher.decrypt(msg).decode('utf-8')
    pad_index = plain_test.find(pad)
    return plain_test[:pad_index]

def tourky_decrypt_CBC(cipher):
    msg=cipher
    pad='{'
    key=key_gen()
    iv='Hmada is awsomee'.encode('utf-8')
    decipher= AES.new(key, AES.MODE_CBC, iv)
    plain_test = decipher.decrypt(msg).decode('utf-8')
    pad_index = plain_test.find(pad)
    return plain_test[:pad_index]

def encrypt_file(filename):
    iv = 'Hmada is awsomee'
    key = key_gen()
    # Reading File
    with open(filename, 'rb')as f:
        plain_file = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv.encode('utf-8'))
    enc_file = cipher.encrypt(plain_file)

    # Writing Encrypted File
    with open(filename + "Encrypted", 'wb') as ef:
        ef.write(enc_file)

def decrypt_file(filename):
    iv = 'Hmada is awsomee'
    key = key_gen()

    # reading encrypted file
    with open(filename, 'rb')as df:
        ecrypted_data = df.read()

    # Decrypting file using cipher
    cipher = AES.new(key, AES.MODE_CBC, iv.encode('utf-8'))
    plain_file = cipher.decrypt(ecrypted_data)

    # Writing a new plain file "decrypted"
    with open(filename + "Decrypted", 'wb') as df:
        df.write(plain_file)



"""
def file_padding (infile):
    fsz = os.path.getsize(infile)
    print ("File Size is: {}".format(fsz))
    with open(infile) as fin:
        while True:
            data = fin.read(2048)
            n = len(data)
            if n == 0:
                break
            elif n % 16 != 0:
                data += '{' * (16 - n % 16)  # <- padded with spaces
        return data
"""