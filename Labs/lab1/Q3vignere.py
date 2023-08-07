plain_text=input("Enter your name: ").upper().replace(" ","")

key=input("Enter the key:").upper().replace(" ","")
key=(key+key* int(len(plain_text)/len(key)))[:len(plain_text)]

alphabets={chr(65+i):i for i in range(26)}
#encryption
encryption=""
for chr_plaintext,k in zip(plain_text,key):
    temp=(alphabets[chr_plaintext]+alphabets[k]) %26
    encryption +=chr(65+temp)
print(encryption)
#decryption
decryption=""
for chr_plaintext, k in zip(encryption,key):
    temp=(alphabets[chr_plaintext]-alphabets[k])%26
    decryption += chr(65+temp)
print(decryption)