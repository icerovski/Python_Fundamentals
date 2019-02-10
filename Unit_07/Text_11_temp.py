# 11. Pyramidic


def key_with_max_val(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def max_val(d):
    return max(d, key=d.get)


# Returns None if does not make at least one loop
def pyramidic(k, base, input_list):
    # Base Case
    if input_list == []:
        return base

    # Recursive Case
    else:
        if k in input_list[0].keys() and input_list[0][k] >= base + 2:
            smaller_list = input_list[1:]
            return pyramidic(k, base + 2, smaller_list)

        elif base > 1: # at least one iteration has happened
            return base


rows = int(input())
data = [input() for i in range(rows)] # Nested Loops in List Comprehension

# Summarize the strings into a list of dictionaries
summary_list = []
from itertools import groupby

for strng in data:
    # Because the source is shared, when the groupby() object is advanced,
    # the previous group is no longer visible. So, if that data is needed later,
    # it should be stored as a list
    groups = groupby(sorted(strng))

    # produces list of tuples
    result = [(label, sum(1 for _ in group)) for label, group in groups]

    # convert list of tuples into dictionary and append it to a list
    summary_list.append(dict(result))

for k in summary_list:
    print(f"{k}", end='\n')

# Identify pyramidic
pyramidic_dict = {}

# skip last index of the list because it cannot start a pyramid
for index in range(0, len(summary_list) - 1):
    for k in summary_list[index].keys():

        # use the next line from the list (index + 1) to start searching
        pyramidic_base = pyramidic(k, 1, summary_list[index + 1:])
        if pyramidic_base:
            if k in pyramidic_dict:
                pyramidic_dict.update({k: max(pyramidic_base, pyramidic_dict[k])})
            else:
                pyramidic_dict.update({k: pyramidic_base})

print(pyramidic_dict)


# for index in range(rows - 1, -1, -1): # reverse loop
#     # key = key_with_max_val(summary_list[index])
#     # value = max_val(summary_list[index])
#     for k in summary_list[index]:
#         if k.value() >= 3