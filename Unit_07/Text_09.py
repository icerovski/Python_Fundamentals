# 9. String Commander
import re


def find_nums(s):
    return list(map(int, (re.findall("\d+", s))))


def rotate(li, x):
    # If x is outside the range [-len(l), len(l)] the function would return
    # the original list. So, introduce remainder because only these rotations
    # will count
    remainder = x % len(li)
    return li[remainder:] + li[:remainder]


line = list(input())
command = input()

while not command == "end":
    act = command.split()[0]
    nums = find_nums(command)

    if act == "Left":
        line = rotate(line, nums[0])

    elif act == "Right":
        line = rotate(line, -1 * nums[0])

    elif act == "Insert":
        index = nums[0]
        insert_str = command.split()[2:]
        line = line[:index] + insert_str + line[index:]

    elif act == "Delete":
        start_index = nums[0]
        end_index = nums[1] + 1
        # removes list element using the index of the element through slicing
        del line[start_index:end_index]

    command = input()

print(f"{''.join(line)}")
