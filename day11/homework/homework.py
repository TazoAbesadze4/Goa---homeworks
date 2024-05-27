# 1) Write a program that takes an input from the user and checks if it's a positive,
#  negative, or zero number using if-else.

num = int(input("enter a number:  "))

if num < 0:
    print("is less than zero")
elif num == 0:
    print("is equal to zero")
else:
    print("is greater than zero")