# 02. Count Real Numbers

# str_list = input().split(' ')
# float_list = []
#
# for str_num in str_list:
#     float_list.append(float(str_num))

float_list = list(map(float, input().split(' ')))
dict_float_occ = {}

def is_in_dict(x):
    if x in dict_float_occ:
        return True

for num in float_list:
    # do not check numbers that are already checked (http://www.tutorialspoint.com/python/python_loop_control.htm)
    if is_in_dict(num):
        pass
    else:
        count = float_list.count(num)
        dict_float_occ[num] = count

# '.items()' returns key and value as lists of tuples
for key, value in sorted(dict_float_occ.items()):
    print(f'{key:.12g} -> {value} times')
