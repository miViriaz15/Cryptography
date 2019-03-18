"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
messagenumbers=[]
keynumbers=[]
command=['j']
while command !='q':
    command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if command=='e':
        message=input("Message: ")
        key=input("Key: ")
        message=list(message)
        for n in message:
            messagenumbers.append(associations.find(n))
        for i in key:
            keynumbers.append(associations.find(i))
        print(messagenumbers)
        print(keynumbers)
    elif command=='d':
        encrypted=input("Message: ")
        key=input("Key: ")
    elif command=='q':
        print("Goodbye!")
    else:
        print("Did not understand command, try again.")
