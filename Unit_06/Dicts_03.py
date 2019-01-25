# 03. Dict-Ref-Advanced

ref_dict = {}
data = input()

while not data == "end":
    name = data.split(" -> ")[0]
    values = data.split(" -> ")[1].split(", ")

    try:
        num_list = list(map(int, values))
        if name not in ref_dict.keys():
            ref_dict[name] = num_list
        else:
            ref_dict[name].extend(num_list) # updates all references

    except ValueError:
        if values[0] in ref_dict.keys():
            ref_dict[name] = ref_dict[values[0]].copy()
        else:
            pass

    data = input()

for k, v in ref_dict.items():
    print(f"{k} === {', '.join(map(str, v))}")

