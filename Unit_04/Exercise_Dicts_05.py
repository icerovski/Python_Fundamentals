# 05. Mixed Phones

phone_book = {}

while True:
    line = input()
    if line == "Over":
        break
    else:
        new_line = line.split(' : ')
        if new_line[0].isdigit():
            name = new_line[1]
            phone = new_line[0]
        else:
            name = new_line[0]
            phone = new_line[1]

        phone_book[name] = phone

for key, value in sorted(phone_book.items()):
    print(f'{key} -> {value}')
