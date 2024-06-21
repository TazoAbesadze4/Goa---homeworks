# 1
# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return
#     arr = [0, 0]
#     for direction in walk:
#         if direction == "n":
#             arr[0] += 1
#         elif direction == "s":
#             arr[1] -= 1
#         elif direction == "w":
#             arr[1] += 1
#         elif direction == "e":
#             arr[1] -= 1
#     return arr == [0, 0]

# 2
# def sort_array(source_array):
#     odd_list = []
#     for i in source_array:
#         if i % 2 != 0:
#             odd_list.append(i)
#     odd_list.sort()
    
#     index = 0
#     result = []
#     for x in source_array:
#         if x % 2 != 0:
#             result.append(odd_list[index])
#             index += 1
#         else:
#             result.append(x)
#     return result

# 3
# def sum_dig_pow(a, b):
#     result = []
#     for num in range(a,b + 1):
#         sum = 0
#         num_str = str(num)
#         for i in range(len(num_str)):
#             sum += int(num_str[i]) ** (i + 1)
#         if sum == num:
#             result.append(num)
#     return result