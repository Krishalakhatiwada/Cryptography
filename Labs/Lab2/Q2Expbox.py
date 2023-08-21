import random as r

expansion_Pbox = [32, 1, 2, 3, 4, 5, 4, 5,
                  6, 7, 8, 9, 8, 9, 10, 11,
                  12, 13, 12, 13, 14, 15, 16,
                  17, 16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25, 24,
                  25, 26, 27, 28, 29, 28, 29,
                  30, 31, 32, 1]

def expandInput(inputText):
    expandedText = ""
    for index in expansion_Pbox:
        expandedText += inputText[index-1]
    return expandedText

input= "11100110011001100110011001100110"
expanded = expandInput(input)

print("input: ", input)
print("After Expansion: ", expanded)