# 04. Rotate List of Strings

list_str = list(input().split(' '))
list_new = []

list_new.append(list_str[len(list_str) - 1])

for i in range(0, len(list_str) - 1):
    list_new.append(list_str[i])

for el in list_new:
    print(f'{el}', end= ' ')
