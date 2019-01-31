# 06.	Diamond Problem

import re

data = input()
d_list = re.findall("<\w+>", data)

if not d_list:
    print("Better luck next time")
else:
    for d in d_list:
        c_list = list(map(int, re.findall(("\d"), d)))
        print(f"Found {sum(c_list)} carat diamond")

        c_list.clear()
