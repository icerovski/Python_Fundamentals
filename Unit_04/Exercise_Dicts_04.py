# 04. Dict-Ref
entries = {}

while True:
    line = input()
    if line == "end":
        break
    else:
        new_line = line.split(' = ')
        name = new_line[0]
        second_name = None

        try:
            second_name = int(new_line[1])
            entries[name] = second_name
        except ValueError:
            second_name = new_line[1]
            if second_name in entries:
                entries[name] = entries[second_name]

for key, value in entries.items():
    print(f'{key} === {value}')
