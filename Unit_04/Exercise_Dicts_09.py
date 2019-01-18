# 09. Wardrobe

from collections import defaultdict
from collections import Counter


def unique(test_list):
    unique_list = []
    for x in test_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


num_of_lines = int(input())
wardrobe = defaultdict(list)
key = None

# Populate dictionary
for a in range(0, num_of_lines):
    line = input().replace(' -> ', ' ').replace(',', ' ').split()
    key = line[0]

    for i in range(1, len(line)):
        wardrobe[key].append(line[i])

# Chosen item from console
line = input().split()
color_pick = line[0]
item_pick = line[1]


for color in wardrobe:
    count_items = dict(Counter(wardrobe[color]))
    item_list = unique(wardrobe[color])

    print(f'{color} clothes:')
    if color == color_pick:
        for item in item_list:
            if item == item_pick:
                print(f"* {item} - {count_items[item]}" + " (found!)")
            else:
                print(f"* {item} - {count_items[item]}")
    else:
        for item in item_list:
            print(f"* {item} - {count_items[item]}")
