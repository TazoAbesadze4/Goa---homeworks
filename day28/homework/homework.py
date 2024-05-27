#   codewars -->

# def solution(s):
#     new_str = ""
#     for i in s:
#         if i.isupper():
#             new_str += " " + i
#         else:
#             new_str += i
#     return new_str


# def is_prime(num):
#     counter = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter += 1
#     if counter != 2:
#         return False
#     return True


# დავ:

# def reverse(st):
#     new_list = []
#     splited_str = st.split()
#     for i in splited_str[::-1]:
#         new_list.append(i)
#     return " ".join(new_list)


# def remove_char(s):
    # return s[1:-1]


# def opposite(number):
#     return -1 * number

# print(opposite(4))


# def positive_sum(arr):
#     sum = 0

#     for i in arr:
#         if i > 0:
#             sum += i
#     return sum


# def century(year):
#     if year % 100 == 0:
#         return year // 100
#     else:
#         return year // 100 + 1


# def make_negative( i ):
#     if i < 0:
#         return i
#     return -i


