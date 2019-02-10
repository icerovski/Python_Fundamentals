# 02. Multiply a List of Integers

list_int = list(map(int, input().split(' ')))
multiplier = int(input())


def multiply(a, b):
    result = a * b
    return result


# list comprehension
multiplied_list = [multiply(el, multiplier) for el in list_int]

for a in multiplied_list:
    print(f'{a}', end= ' ')

