# 09. Sort Numbers

num_list = list(map(int, input().split(' ')))
num_list.sort()

str_list = list(map(str, num_list))
print(" <= ".join(str_list))