#ITS100 Homework2 Problem3
word = input("Input a word: ")
point = 0
if word.isalpha():
    for i in word:
        if i.upper() in "AEILNORSTU":
            point += 1
        elif i.upper() in "DG":
            point += 2
        elif i.upper() in "BCMP":
            point += 3
        elif i.upper() in "FHVWY":
            point += 4
        elif i.upper() in "K":
            point += 5
        elif i.upper() in "JX":
            point += 8
        elif i.upper() in "QZ":
            point += 10
    print("Output: %d"%point)
else: 
    print("Invalid input")
        
        
#To use True & False to check for invalid input
"""
word = input("Input a word: ")
point = 0
for i in word:
    if i.isalpha():
        check = True #To check for invalid input
        if i.upper() in "AEILNORSTU":
            point += 1
        elif i.upper() in "DG":
            point += 2
        elif i.upper() in "BCMP":
            point += 3
        elif i.upper() in "FHVWY":
            point += 4
        elif i.upper() in "K":
            point += 5
        elif i.upper() in "JX":
            point += 8
        elif i.upper() in "QZ":
            point += 10
    else:
        check = False
if check == True: #If True then it prints output
    print("Output: %d"%point)
else: #If False then let it prints Invalid
    print("Invalid input")
    
"""