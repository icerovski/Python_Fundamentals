# 02. Split by Word Casing

separators = (' ', ',', ';', ':', '.', '!', '(', ')', '"', "'", '\\', '/', '[', ']')
text = input()
lower_case = []
upper_case = []
mixed_case = []

def my_split(txt, seps):
    default_sep = seps[0]

    # skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)

    return [i.strip() for i in txt.split(default_sep)]


new_text = list(filter(None, my_split(text, separators)))

for item in new_text:
    if all(ch.islower() for ch in item):
        lower_case.append(item)
    elif all(ch.isupper() for ch in item):
        upper_case.append(item)
    else:
        mixed_case.append(item)

print(f"""Lower-case: {', '.join(lower_case)}
Mixed-case: {', '.join(mixed_case)}
Upper-case: {', '.join(upper_case)}""")

