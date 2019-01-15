# 10. Square Numbers

from math import sqrt

num_list = list(map(int, input().split(' ')))
num_list.sort()

def is_square(n):
    return n > -1 and sqrt(n) % 1 == 0

new_num_list = [el for el in reversed(num_list) if is_square(el)]
str_list = list(map(str, new_num_list))

print(" ".join(str_list))