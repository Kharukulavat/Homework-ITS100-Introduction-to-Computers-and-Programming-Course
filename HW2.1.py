#ITS100 Homework2 Problem1
from math import*
v = input("Input v: ")
i = 1
S = 0
while S <= float(v):
    try:
        v = float(v)
        a = (sqrt(2)*i)-1
        i += 1
        S += a
    except:
        print("Invalid input")
        break
if S > 0: #To make it print only when it calculates
    print("Output: n = %d, S = %.2f"%(i-1,S)) #i - 1 because we stop when S > v then i would be 1 exceeds (after i =4, i += 1 then the loop will stop so i will be 1 exceeds)
print(i)
    