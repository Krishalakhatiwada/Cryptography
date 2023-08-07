plain_text=input("Enter a string:").upper().replace(' ','')



key=5

alphabets={chr(65+i):i for i in range(26)}

rev_alphabets={value:key for key,value in alphabets.items()}
cipher_text=""
#encryption
for letter in plain_text:
    encrypt_num= (alphabets[letter] +key)%26
    # print(encrypt_num)
    cipher_text+=rev_alphabets[encrypt_num]

print(cipher_text)
decipher_text=""
for letter in cipher_text:
    decrypt_num=(alphabets[letter]- key)%26
    decipher_text+=rev_alphabets[decrypt_num]

print(decipher_text)