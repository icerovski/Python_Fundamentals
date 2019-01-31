# 03.	Text filter

ban_list = input().split(" ")
text = input()

for el in ban_list:
    text = text.replace(el, "*"*len(el))

print(text)