# 1) განვიხილოთ ეს კოდი -->

# def find_last_even(numbers_list):
#     for i in range(len(numbers_list) - 1, -1, -1):
#         if numbers_list[i] % 2 == 0:
#             return numbers_list[i]

# print(find_last_even([1,2,3,4,5]))

# 2) მოვაშოროთ ტერმინაში გამოტანილი პირველი პლიუსი -->

# def my_join(join_str, strings_list):
#     joined_elemnts = ''
    
#     for word in strings_list:
#         joined_elemnts += join_str + word
    
#     return joined_elemnts

# print(my_join("+", ["1","2","3"])) 