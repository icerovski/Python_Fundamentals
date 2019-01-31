# 05.	Value of a String

import re
# from functools import reduce

lst, case = input(), input()

if case == "LOWERCASE":
    # finds all lowercase letters and returns a list of one-letter strings
    strip_list = re.findall("[a-z]", lst)
elif case == "UPPERCASE":
    strip_list = re.findall("[A-Z]", lst)

# make a list with the ASCII numbers of the strings
dig_list = [ord(el) for el in strip_list]

# sum the list of integers through reduce function
# dig_list_sum = reduce(lambda a, b: a + b, dig_list)

print(f"The total sum is: {sum(dig_list)}")