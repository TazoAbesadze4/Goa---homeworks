# def my_range(start, end, step):
#     numbers = []

#     while start < end:
#         numbers.append(start)
#         start = start + step
    
#     return numbers

# print(my_range(0,10 + 1,2))


# 1) შექმენით პროგრამა, სადაც ბოლოდან პირველ ოთხის 
# ჯერად რიცხვს გამოიტანთ სიიდან. მაგ სიაში კი 
# 10-იდან 50-ის ჩათვლით უნდა იყოს რიცხვები

# numbers = []

# for i in range(10, 50 + 1):
#     numbers.append(i)

# # Second Part

# def func(numbers):
#     for index in range(len(numbers) - 1, -1, -1):
#         if numbers[index] % 4 == 0:
#             return numbers[index]

# print(func(numbers))


# 2) შექმენით range-ის მსგავსი ფუნქცია, სადაც მესამე 
# არგუმენტი იქნება მომხმარებლის მიერ შეტანილი. 
# აგრეთვე კომენტარით აღწერეთ return

# def num(first, last, step=1):
#     my_list = []
#     while first < last:
#         my_list.append(first)
#         first += step
#     return my_list

# print(num(0, 10, 2))


# 2) შექმენით ფუნქცია სახელად filter, მისი პირველი პარამეტრი 
# იქნება კოლექცია, მეორე კი მნიშვნელობა. თქვენი დავალებაა, რომ 
# კოლექციიდან ამოიღოთ ეგ კონკტეტული მნიშვნელობები და 
# დააბრუნოთ ის



# 3) შექმენით ფუნქცია, რომელსაც გადასცემთ 
# მართკუთხა სამკუთხედის კათეტებს, თქვენი 
# დავალება კი არის ის, რომ დააბრუნოთ ჰიპოტენუზა.
# a^2 + b^2 = c^2

kateti1 = 20
kateti2 = 20

hipotenuza = kateti1 * 2

print(hipotenuza)

# 4) შექმენით ფუნქცია, რომელსაც გადაეცემა თქვენი სახელი.
# თუ სახელის სიგრძე აღემატება ხუთს, დააბრუნეთ მისი uppercase 
# ვარიანტი.ხოლო თუ ნაკლებია ან ტოლია მისი, დააბრუნეთ capitalize
# ვარიანტი


