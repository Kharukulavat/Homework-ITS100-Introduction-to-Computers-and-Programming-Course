#ITS100 Homework1 Problem3
ft = float(input("Input the number of feet: "))
inch = float(input("Input the number of inches: "))
incm = inch*2.54
ftcm= ft*12*2.54
height = incm+ftcm
print("The height in cm = %.2f"%height)