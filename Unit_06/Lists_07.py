# 07. Sort List Using Bubble Sort*
def bubble_sort(a_list):
    swapping = True
    pass_count = len(a_list) - 1
    while pass_count > 0 and swapping:
        swapping = False
        for i in range(0, pass_count):
            if a_list[i] > a_list[i + 1]:
                swapping = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        pass_count = pass_count - 1


nums = list(map(int, input().split()))
bubble_sort(nums)
print(f"{' '.join(map(str, nums))}")
