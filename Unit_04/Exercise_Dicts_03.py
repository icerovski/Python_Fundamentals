# 03. Letter Repetition

str_line = input()
counts = {}

def is_in_dict(a):
    if a in counts:
        return True

for char in str_line:
    if is_in_dict(char):
        pass
    else:
        count = str_line.count(char)
        counts[char] = count

# '.items()' returns key and value as lists of tuples
for key, value in counts.items():
    print(f'{key} -> {value}')
