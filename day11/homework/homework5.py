# 6) Write a program that asks the user for their age and prints
#   a message based on the
# age range (e.g., "Child", "Teenager", "Adult") 
#   using if-elif-else.

age = int(input("please enter your age: "))

if age < 0:
    print("this age doesn't exist")
elif age <= 10:
    print("you are a child")
elif age < 20:
    print("you are a teen")
else:
    print("you are an adult")