# 1
# def solution(string):
#     return string[::-1]

# 2
# def repeat_str(repeat, string):
#     return repeat * string

# 3
# def sum_two_smallest_number(numbers):
#     sorted_numbers = sorted(numbers)
#     return sorted_numbers[0] + sorted_numbers[1]

# 4
# def max_multiple(divisor, bound):
#     if bound % divisor == 0:
#         return bound
    
#     multiples = []
    
#     for num in range(divisor, bound):
#         if num % divisor == 0:
#             multiples.append(num)
    
#     return max(multiples)

# 5
# def check_exam(correct_answers,test_answers):
#     score = 0
    
#     for index in range(len(correct_answers)):
#         if correct_answers[index] == test_answers[index]:
#             score = score + 4
#         elif test_answers[index]  == "":
#             score = score + 0
#         else:
#             score = score - 1
    
#     if score < 0:
#         return 0
#     else:
#         return score

# 6
# def row_weights(array):
#     even_sum = 0
#     odd_sum = 0
    
#     for index in range(len(array)):
#         if index % 2 == 0:
#             even_sum = even_sum + array[index]
#         else:
#             odd_sum = odd_sum + array[index]
    
#     return [even_sum, odd_sum]