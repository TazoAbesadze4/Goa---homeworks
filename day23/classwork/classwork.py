# replace - ჩვენ შეგვიძლია სტრინგს გადავცეთ 2 სიმბოლოს.
#  1 სიმბოლო - რა გვინდა შევცვალოთ
#  2 სიმბოლო - რითი გვინდა რომ შევცვალოთ


# name = "tazo"
# names = name.replace("o", "u") 
# print(names)
# ტერმინალში გამოიტანს "tazu"-ს


# print("tazo".replace("o", "u"))


# word = "tazoabesadze"
# print(word.replace("a", "k"))


# word = "tazoabesadze5"
# print(word.replace("5", "2"))


# def my_replace(word, replace_char, input_char):
#     changed_word = ''

#     for char in word:
#         if char == replace_char:
#             changed_word = changed_word + input_char
#         else:
#             changed_word = changed_word + char
    
#     return changed_word

# print(my_replace("lukaak", "a", "d"))



# "luuuka".count("u") --> result: 3         -->

# def my_count(collection, count_element):
#     count = 0
    
#     for element in collection:
#         if element == count_element:
#             count = count + 1
    
#     return count

# print(my_count("luuuka", "u"))



# def my_find(collection, value):
#     for index in range(len(collection)):
#         if collection[index] == value:
#             return index
#     return -1

# print(my_find([1,2,3,4,5], 3))



# def my_find(collection, value):
#     for index in range(len(collection)):
#         if collection[index] == value:
#             return index
#     return -1

# print(my_find(["tazo"], "z"))


#   ------>>>>>...>>>>>>


# 1)შექმენით პროგრამა სადაც გექნებათ მოცემული სია, და უნდა დაითვალოთ 
# ამ სიაში ლუწი რიცხვები

# def count_evens(numbers_list):
#     count = 0
    
#     for number in numbers_list:
#         if number % 2 == 0:
#             count = count + 1
    
#     return count

# print(count_evens([1,2,3,4,5,6]))


# 2) შექმენით პროგრამა სადაც გექნებათ მოცემული სტრინგი, ხოლო ლუწ ინდექსებზე მყოფი 
# ელემენტები ჩაანაცვლეთ სხვა სიმბოლოთი ან სხვა რიცხვით

# def replace_even_indexes(word,replace_char):
#     changed_word = ''
    
#     for index in range(len(word)):
#         if index % 2 == 0:
#             changed_word = changed_word + replace_char
#         else:
#             changed_word = changed_word + word[index]
            
#     return changed_word


# print(replace_even_indexes("lukaa", "k"))

# 3) იპოვეთ სიაში ბოლო ლუწი რიცვხის ინდექსი
    


# 4) გადმოგეცემათ რიცხვთა სია ფუნქციაში, თვქენი დავალებაა ამ სიაშ მყოფი ლუწი რიცხვები 
# შეართოთ + ის მეშვეობით და დააბრუნოთ საბოლოო შედეგად სტრინგი,
#  შესატანი მონაცემი: [1,2,3,4],

# საბოლოო შედეგი: "2+4"

# გაითვალისწინეთ ის რომ თუ სიაში ერთი ლუწი რიცხვია, დააბრუნეთ პირდაპირ

# ხოლო თუ არარის სიაში ლუწი რიცხვი მაშინ დააბრუნეთ ცარიელი სტრინგი

