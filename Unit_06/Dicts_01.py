# 01. Key-Key Value-Value

key = input()
value = input()
n = int(input())
test_dict = {}

for i in range(0, n):
    line = input()
    dict_key = line.split(" => ")[0]
    dict_list = line.split(" => ")[1].split(";")

    if not dict_key in test_dict.keys():
        test_dict[dict_key] = dict_list
    else:
        test_dict[dict_key].append(dict_list)

for k in test_dict.keys():
    if key in k:
        print(f"{k}:")
        for each in test_dict[k]:
            if value in each:
                print(f"-{each}")
