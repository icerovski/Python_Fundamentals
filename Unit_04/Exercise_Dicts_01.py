# 01. Odd Occurrences

# converts all cases to low
line = input().lower()
words = line.split(' ')

counts = {}

def is_in_dict(str):
    if str in counts:
        return True

def odd_occ(n):
    if n % 2 != 0:
        return True

for word in words:
    if is_in_dict(word):
        pass
    else:
        count = words.count(word)
        if odd_occ(count):
            counts[word] = count

print(", ".join(counts.keys()))
