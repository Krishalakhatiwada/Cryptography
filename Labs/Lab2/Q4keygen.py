import random as r
 
paritydrop = [57, 49, 41, 33, 25, 17,  9,  1,
               58, 50, 42, 34, 26, 18, 10,  2,
               59, 51, 43, 35, 27, 19, 11,  3,
               60, 52, 44, 36, 63, 55, 47, 39,
               31, 23, 15,  7, 62, 54, 46, 38,
               30, 22, 14,  6, 61, 53, 45, 37,
               29, 21, 13,  5, 28, 20, 12,  4]
 
compressionbox = [14, 17, 11, 24,  1,  5,
                    3,  28, 15,  6, 21, 10,
                    23, 19, 12,  4, 26,  8,
                    16,  7, 27, 20, 13,  2,
                    41, 52, 31, 37, 47, 55,
                    30, 40, 51, 45, 33, 48,
                    44, 49, 39, 56, 34, 53,
                    46, 42, 50, 36, 29, 32]
 
def setInputBlock():
    input_block = ""
    for _ in range(64):
        input_block += str(r.randint(0,1))
    return input_block
 
def generate_key(input):
    round = 1
    
    key = ""
    for i in paritydrop:
        key += input[i-1]
    
    initial_bits = key[:28]
    last_bits = key[28:]
    
    
    while(round <= 16):
        if(round == 1 or round == 2 or round == 9 or round == 16):
            
            initial_bits = initial_bits[1:] + initial_bits[0]
            last_bits = last_bits[1:] + last_bits[0]
            
        else:
            initial_bits = initial_bits[2:] + initial_bits[:2]
            last_bits = last_bits[2:] + last_bits[:2]
 
        result = ""
        join = initial_bits + last_bits
        for i in compressionbox:
            result += join[i-1]
        print("For Round:", round, "Key is: ", result)
        round += 1
 
input = setInputBlock()
generate_key(input)
