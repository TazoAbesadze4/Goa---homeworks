# 3)Write a program that calculates the sum of a number entered by the user
#  using a while loop.

calculation_made = False
x = int(input("please enter first namber: "))
y = int(input("please enter second namber: "))

while calculation_made != True:
    print(x + y)
    calculation_made = True
