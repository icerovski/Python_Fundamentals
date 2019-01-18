wardrobe_dict = dict()
num_lines = int(input())

for i in range(num_lines):
    line = input()
    colour, clothes_str = line.split(' -> ')
    clothes_list = clothes_str.split(',')

    if colour not in wardrobe_dict:
        wardrobe_dict[colour] = dict()

    for garment in clothes_list:
        if garment not in wardrobe_dict[colour]:
            wardrobe_dict[colour][garment] = 1
        else:
            wardrobe_dict[colour][garment] += 1

# target_colour, target_garment = input().split(' ')
target_input = input().split(' ')
target_colour, target_garment = target_input[0], target_input[1]

for colour, clothes_dict in wardrobe_dict.items():
    print(f'{colour} clothes:')

    for garment, count in clothes_dict.items():
        if colour == target_colour and garment == target_garment:
            print(f'* {garment} - {count} (found!)')
            continue

        print(f'* {garment} - {count}')