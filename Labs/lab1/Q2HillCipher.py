print=input("Enter your name:").upper().replace(' ','')

key=[[2, 4], [3,5]]

alphabets={chr(65+i):i for i in range(26)}
rev_alphabtes={value:key for key,value in alphabets.items()}
