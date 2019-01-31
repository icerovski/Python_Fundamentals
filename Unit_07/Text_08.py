# 08.	Deserialize String

line = input()
char_dict = {}

while not line == 'end':
    char = line.split(':')[0]
    indices = line.split(":")[1].split("/")

    for el in indices:
        if not int(el) in char_dict:
            char_dict[int(el)] = char
        else:
            char_dict[int(el)].upper(char)

    line = input()

for index, char in sorted(char_dict.items()):
    print(f"{char}", end='')
