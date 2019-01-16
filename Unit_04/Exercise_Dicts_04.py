# 04. Dict-Ref
entries = {}


def in_dict(ch):
    if ch in entries:
        return True


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
            if in_dict(second_name):
                entries[name] = entries[second_name]

for key, value in entries.items():
    print(f'{key} === {value}')
