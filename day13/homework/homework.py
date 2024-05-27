# 1) Write a program that prints numbers from 1 to 10 using a while loop.

i = 1

while i <= 10:
    print(i)
    i += 1


# 2) Write a program that prints the even numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

# 3) Write a program that asks the user to enter a number and then prints whether the number is positive, 
#       negative, or zero using an if-else statement.

num = float(input("please enter your number: "))
if num < 0:
    print("The number is less than zero")
elif num > 0:
    print("The number is greater than zero")
else:
    print("The number is zero")

# 4) Write a program that asks the user to enter a password. If the password is "abc123", print "Access granted";
#        otherwise, print "Access denied".

password = ""
while password != "abc123":
    password =input("enter your password: ")

    if password == "abc123":
        print("Access granted")
    else:
        print("Access denied")

# 5) Write a program that prints numbers from 1 to 10, but stops if the number is 5 using a while loop and the break statement. break

i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 6:
        break

# 6) Write a program that asks the user to enter a number between 1 and 5. If the number is less than 1 or greater than 5, print "Invalid input". 
#       If the number is between 1 and 5, print "Valid input".

num = int(input("enter your number 1 to 5: "))

if num >= 1 and num <= 5:
    print("Valid input")
else:
    print("Invalid input")

# 7) Write a program that asks the user to enter a number. If the number is divisible by 3, print "Fizz". 
# If the number is divisible by 5, print "Buzz". If the number is divisible by both 3 and 5, print 
#  "FizzBuzz". Otherwise, print the number itself.

num = int(input("please enter the number: "))
if num %3 == 0 and num %5 == 0:
    print("FizzBuzz")
elif num %3 == 0:
    print("Fizz")   
elif num %5 == 0:
    print("Buzz")
else:
    print(num)
    
