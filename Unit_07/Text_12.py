# 12.	Nilapdromes *

line = input()
while not line == "end":

    # Find the size of the border
    index_a = 0
    index_b = len(line) // 2
    size = 0
    while 0 < index_b < len(line):
        if ord(line[index_a]) == ord(line[index_b]):
            index_a = index_a + 1
            size = size + 1

        else:
            if size > 0:
                index_a = 0
                index_b = index_b - size
                size = 0

        index_b = index_b + 1

    # Find the size of the core
    core_size = len(line) - 2 * size

    # Test if string is nilapdrome
    if size != 0 and core_size != 0:
        border = line[0:size]
        core = line[size:size + core_size]

        print(core + border + core)

    line = input()
