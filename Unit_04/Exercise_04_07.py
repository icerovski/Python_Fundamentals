# 07. Remove Negatives and Reverse

num_list = list(map(int, input().split(' ')))
new_num_list = []

for el in reversed(num_list):
    if el >= 0:
        new_num_list.append(el)

list_full = len(new_num_list) != 0

if list_full:
    for el in new_num_list:
        print(f'{el}', end= ' ')
else:
    print("empty")