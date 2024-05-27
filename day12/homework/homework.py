# 2)  Calculate the sum of all even numbers from 1 to 10 using a while loop:

# 3) while ციკლის მეშვეობით შეამოწმეთ რიცხვები 1 დან 20 ჩათვლით,
#  რიცხვი თუ იყოფა 3 და 5 ზე მაშინ დაპრინტეთ ეგ რიცხვი

# 4) for ციკლის მეშვეობით დაბეჭდეთ ყველა რიცხვი 1-100 ჩათვლით რომელიც იყოფა 5 ზე

# 5) for ციკლის მეშვეობით დაბეწეთ ყველა ის ირცხვი რომელიც იყოფა
#  6_ზე 1 დან 20 ის ჩათვლით


# 2)

num = 1
sum_even = 0
num = 1
sum_even = 0

while num <= 10:
    if num %2 == 0:
        sum_even += num 
    num += 1 
print(sum_even)



# 3)

i = 1
i = 1

while i  <= 20:
    if i %3 == 0 and i %5 == 0:
        print(i)
    i += 1
while i  <= 20:
    if i %3 == 0 and i %5 == 0:
        print(i)
    i += 1

# 4)

for i in range(1, 101):
    if i %5 == 0:
        print(i)
for i in range(1, 101):
    if i %5 == 0:
        print(i)


# 5)

for i in range(1, 20):
    if i %6 == 0:
        print(i)