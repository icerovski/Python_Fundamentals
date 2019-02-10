# 12.	Nilapdromes *
import difflib

line = input()
while not line == "end":
    mid = len(line) // 2
    a = line[:mid]
    b = line[mid:]

    matches = difflib.SequenceMatcher(None, a, b).get_matching_blocks()

    # call triple/tuple (a, b, size)
    # border_start = matches[0].a
    border_length = matches[0].size
    core_length = len(line) - 2 * border_length
    # beg_border = line[0:border_length]
    # end_border = line[-border_length:]

    if line[0:border_length] == line[-border_length:] and core_length != 0:
        border = line[0:border_length]
        core = line[border_length:border_length + core_length]

        print(core + border + core)

    line = input()
