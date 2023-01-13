#ITS100 Homework2 Problem2
digit = input("Input 12-digit string: ")
count = 0
s = 0
if digit.isnumeric():
    if len(digit) == 12:
        for i in digit:
            i = int(i)
            count+=1
            if count%2 != 0:
                s += i*1
            else:
                s += i*3
        t = 10 - (s%10)
        if t == 10:
            t = 0
            c = t
        else:
            c = t
        print("Output: check digit = %d"%c)
    else:
        print("invalid input")
else:
    print("invalid input")