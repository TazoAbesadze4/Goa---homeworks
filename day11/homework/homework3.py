# 5)Write a program that simulates a simple login system.
#   Ask the user for a username and password, 
#   and if they enter "admin" and "password123", 
# respectively, print "Login successful" using if-else.

balance = 100
pin = 55

user_input = int(input("please enter your pin: "))
if user_input == pin:
    print("pin is correct")
    x = input("do you wish to withdraw money or check balance? ")
    if x == "check balance":
        print("your balance is " + str(balance) + " dolars")
    elif x == "withdraw money":
        print("you withdrew 50 dolar")
else:
    quit()        