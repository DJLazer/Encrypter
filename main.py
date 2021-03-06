from crypting import encrypt, decrypt
import os

while True:
    choice = input("Type 1 for encryption or 2 for decryption: ")
    if choice == str(1):
        a = input("Enter the text you want encrypted: ")
        b = encrypt(a)
        print("Encryption: " + b)
        os.system("PAUSE")
    elif choice == str(2):
        a = input("Enter the text you want decrypted: ")
        b = decrypt(a)
        print("Decryption: " + b)
        os.system("PAUSE")
