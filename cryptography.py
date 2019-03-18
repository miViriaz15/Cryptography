"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
while command !='q':
    if command=='e':
        message=input("Message: ")
        key=input("Key: ")
    elif command=='d':
        encrypted=input("Message: ")
        key=input("Key: ")
    else:
        print("Did not understand command, try again.")
        command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
if command=='q':
        print("Goodbye!")