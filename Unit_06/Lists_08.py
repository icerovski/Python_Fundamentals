# 08. Sort List Using Insertion Sort*


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        cur_val = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > cur_val:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = cur_val


nums = list(map(int, input().split()))
insertion_sort(nums)
print(f"{' '.join(map(str, nums))}")
