# 10. Shellbound

from collections import defaultdict
from math import ceil

shell_dict = defaultdict(list)


def funct(l):
    int_list = list(map(int, l))
    result = sum(int_list) - (sum(int_list) / len(int_list))
    rounded_result = ceil(result)
    return rounded_result


while True:
    line = input().split()
    if line[0] == "Aggregate":
        break

    else:
        region, shell = line[0], line[1]

        if shell not in shell_dict[region]:
            shell_dict[region].append(shell)

for key, value in shell_dict.items():
    giant_value = funct(shell_dict[key])
    print(f"{key} -> {', '.join(value)} ({giant_value})")
