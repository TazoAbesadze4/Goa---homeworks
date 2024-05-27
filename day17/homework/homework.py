# len - ზომა (კოლექციის)

# 1 - Write a function that takes a list of numbers as input and 
# returns the sum of all the numbers in the list.

# def calculate_sum(number):
#     total = 0

#     for i in number:
#         total += i
#     return total

# list = [1,2,3,4,5]
# print(calculate_sum(list))

# 2 -  Write a function that takes a list of strings as input
#  and returns a new list containing only the strings that have 
# a length greater than 5.

# def filter_string(strings):
#     result = []

#     for i in strings:
#         if len(i) > 5:
#             result.append(i)
#     return result

# list = ["banana", "orange", "apple", "kiwi"]
# string = filter_string(list)
# print(string)

# # 3 -  Write a function that takes a list of numbers as input 
# # and returns a new list containing only the even numbers from 
# # the original list.

# def even_numbers(numbers):
#     numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             numbers.append(num)
#     return numbers

# # Example usage:
# my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered_numbers = even_numbers(my_numbers)
# print(filtered_numbers)

# # 4 -  Write a function that takes a list of numbers as input 
# # and returns the largest number in the list.

# def big_number(num):
#     return max(num)

# list = [1,2,3,4,5,6,7,8,9,10]
# print(big_number(list))

# # 5 -  Write a function that takes a list of strings as input 
# # and returns a new list containing only the strings that start 
# # with the letter 'a'.

# def starting_with_a(strings):
#     result = []
#     for i in strings:
#         if i[0] == 'a':
#             result.append(i)
#     return result

# # Example usage:
# list = ["apple", "banana", "kiwi", "orange", "apricot"]
# filtered_strings = starting_with_a(list)
# print(filtered_strings)

# 6 - Write a function that takes a list of 
# numbers as input and returns a new list 
# containing the square of each number.

# def square_numbers(numbers):
#     squared_numbers = []
#     for i in numbers:
#         squared_numbers.append(i ** 2)
#     return squared_numbers

# my_numbers = [1, 2, 3, 4, 5]
# squared_numbers = square_numbers(my_numbers)
# print(squared_numbers)

# # 7 -  Write a function that takes a list of 
# strings as input and returns a new list 
# containing the lengths of each string.

# def string_lengths(strings):
#     lengths = []
#     for i in strings:
#         lengths.append(len(i))
#     return lengths

# # Example usage:
# my_strings = ["apple", "banana", "kiwi", "orange", "apricot"]
# string_lengths_list = string_lengths(my_strings)
# print(string_lengths_list)

# # 8 -  Write a function that takes a list of 
# numbers as input and returns the sum of all the
# numbers that are greater than 10. 

# def sum_numbers_greater_than_10(numbers):
#     total = 0
#     for i in numbers:
#         if i > 10:
#             total += i
#     return total

# my_numbers = [5, 12, 3, 15, 8, 9, 20]
# result = sum_numbers_greater_than_10(my_numbers)
# print(result)
