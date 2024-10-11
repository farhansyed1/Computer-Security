#!/usr/bin/env python3
from insecure_hash import hash_string
from Cryptodome.Cipher import AES
import os

def find_collision(message):
    hashedMessage = hash_string(message) # Get the hash value
    key = b'FARHAN0123456789'  # Set a fixed 16-byte key
    cipher = AES.new(key, mode=AES.MODE_ECB) # Cipher using fixed key
    encryptedHash = cipher.encrypt(hashedMessage) # Encrypt the hashed message
    return encryptedHash + key # Message that results in collision is the encrypted hash and the key appended together 

if __name__ == '__main__':
    message = b"aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb"
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))
