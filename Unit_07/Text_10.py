# 10.	Stateless


def collapse_state(txt, del_str):
    counter = 0
    index = 0
    last_index = len(txt) - len(del_str) + 1
    cur_txt = "".join(txt)
    cur_del_str = "".join(del_str)

    while index < last_index:
        if cur_del_str == cur_txt[index:index + len(del_str)]:
            position = index - counter
            del states[position:position + len(del_str)]
            counter = counter + len(del_str)
            index += len(del_str)
        else:
            index += 1


states = list(input())

while not "".join(states) == "collapse":

    fiction = list(input())

    while fiction:
        collapse_state(list(states), fiction)
        # delete first and last elements of the list
        fiction = fiction[1:-1]

    if states:
        print(''.join(states).strip())
    else:
        print("(void)")

    states = list(input())

