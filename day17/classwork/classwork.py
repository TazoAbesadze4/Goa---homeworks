def welcome(name, lastname):
    print("welcome " + name + " " + lastname)

welcome(input("enter your name: "), input("enter your lastname: "))

#  დავალება: შექმნეთით ფუნქცია რომელშიც  ჩაშენებული იქნება for
#  ციკლი, ფუნქციას გაუწერეთ პარამეტრი რომელსაც ექნება სახელად 
# iteration. შემდეგ range ში პირდაპირ რიცხვის მაგივრადჩაწერეთ 
# ამ პარამეტრის სახელი და გამოიძახეთ სამჯერ სხვადასხვა მნიშვნელობით

def num(interation):
    for i in range(interation):
        print("tazo")

num(3)


#  - -  -------------  sxva -->

def multiply(num1, num2):
    return num1 * num2

print(multiply(5, 3))


# შექმენით 4 ფუნქცია რომლებიც გააკეთებს მიმატებას გამოკლებას
#  გამრავლებას და გაყოფას, შემდეგ კი შედეგი უნდა დააბრუნოს 
#   ფუნქციამ return keyword ის გამოყენებით, გამოიძახეთ თითოეული 
#    ფუნქცია

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


print(add(5,5))
print(subtract(5,5))
print(multiply(5,5))
print(divide(5,5))


#   -->-->-->

numbers = [1,2,3,4,5]

numbers.append(input("gtxovt daamatot ricxvi siashi: "))

print(numbers)

# -->-->-->

numbers = []
for i in range(30):
    numbers.append(i)

print(numbers)
