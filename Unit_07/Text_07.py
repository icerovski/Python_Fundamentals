# 07.	Serialize String

str_input = input()
str_dict = {}

# find all indices of the same character in a string
def all_indices(string, sub, list_index=[], offset=0):
    list_index.clear()
    # returns the index of the first occurrence of the character
    i = string.find(sub, offset)
    while i >= 0:
        list_index.append(i)
        i = string.find(sub, i + 1)
    return list_index


for ch in str_input:
    if ch not in str_dict:
        # the built-in 'list' function ensures that the list is copied
        # if only equal sign, the new list will point to the same reference
        str_dict[ch] = list(map(str, all_indices(str_input, ch)))
    #
    # else:
    #     continue

for k, v in str_dict.items():
    print(f"{k}:{'/'.join(v)}")
