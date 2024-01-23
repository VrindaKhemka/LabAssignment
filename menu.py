from Calc import *

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
n = int(input('Enter a choice:'))
if n == 1:
    add(a,b)
elif n==2:
    subtract(a,b)
elif n==3: 
    multiply(a,b)
else:
    divide(a,b)