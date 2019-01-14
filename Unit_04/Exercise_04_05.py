# 05. Count of Odd Numbers in List

num_list = list(map(int, input().split(' ')))

def is_odd(num_list):
    counter = 0
    for el in num_list:
        if el % 2 == abs(1):
            counter += 1
    return counter

print(is_odd(num_list))