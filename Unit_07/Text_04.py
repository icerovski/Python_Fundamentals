# 4.	Palindromes


def my_split(txt, seps):
    default_sep = seps[0]

    # skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)

    return [i.strip() for i in txt.split(default_sep)]


text = input()
separators = [' ', ',']

str_list = my_split(text, separators)
output_list = []

for el in str_list:
    if el == el[::-1] and el not in output_list:
        output_list.append(el)

print(", ".join(sorted(output_list, key=str.lower)))

