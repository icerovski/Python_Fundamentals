# 02. Multiply a List of Integers

list_int = list(map(int, input().split(' ')))
multiplier = int(input())
# print(list_int)
# print(multiplier)

# new_list_int = []

def multiply(a, b):
    result = a * b
    return result

# Multiply List
# for x in list_int:
#     a = multiply(x, multiplier)
#     new_list_int.append(a)

# print(new_list_int)

multiplied_list = [multiply(el, multiplier) for el in list_int]

# Print Result
# print(' '.join(multiplied_list))

for a in multiplied_list:
    print(f'{a}', end= ' ')

