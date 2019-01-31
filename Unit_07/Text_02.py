# 02.	Count substring occurrences

text, key = input(), input()
counter = 0

for index in range(0, len(text) - len(key) + 1):
    if key.lower() == text[index:index + len(key)].lower():
        counter += 1

print(counter)