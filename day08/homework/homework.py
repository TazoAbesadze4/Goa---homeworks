# 2) for loop'ით და while loop'ით ეცადეთ გამოიტანოთ
#  რიცხვები 1'დან 100-ის ჩათვლით

#  1 ->

for i in range(1,101):
    print(i)

#  2 ->

num = 1

while num <= 100:
    print(num)
    num += 1

# 3) for ციკლის მეშვეობით შეკრიბეთ პირველი 10 რიცხვი
    
sum = 0

for i in range(11):
    sum += i

print(sum)


# 4) for ციკლის მეშვეობით გამოიტანეთ ლუწი რიცხვები
#  1'დან 20'ის ჩათვლით

# way 1

for i in range(0, 20, 2):
    print(i)

# way 2

for i in range(21):
    if i %2 == 0:
        print(i)