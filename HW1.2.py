#ITS100 Homework1 Problem2
cost = float(input("Input the cost of a meal: "))
svc = 0.1*cost
sum = cost+svc
vat = 0.07*sum
allsum = sum+vat
print("Service charge = %.2f THB"%svc)
print("VAT = %.2f THB"%vat)
print("Total cost = %.2f THB"%allsum)