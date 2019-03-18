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
mkcombinednumbers=[] #message and key combined numbers
command=['j']
encrypted=[]
while command !='q':
    command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if command=='e':
        message=input("Message: ")
        key=input("Key: ")
        message=list(message)
        key=list(key)
        for n in message:
            messagenumbers.append(associations.find(n))
        for i in key:
            keynumbers.append(associations.find(i))
        print(messagenumbers)
        print(keynumbers)
        for k in range(0,len(messagenumbers)):
            mkcombinednumbers.append(messagenumbers[k]+keynumbers[k%len(keynumbers)])
        print(mkcombinednumbers)
        for l in mkcombinednumbers:
            encrypted.append(associations[l])
            print(encrypted)
    elif command=='d':
        encrypted=input("Message: ")
        key=input("Key: ")
    elif command=='q':
        print("Goodbye!")
    else:
        print("Did not understand command, try again.")
        