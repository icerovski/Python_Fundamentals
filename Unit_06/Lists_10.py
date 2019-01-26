# 10. Largest N Items*


def rev_sort(aList):
    for index in range(1, len(aList)):
        cur_val = aList[index]
        position = index

        while position > 0 and cur_val > aList[position - 1]:
            aList[position] = aList[position - 1]
            position = position - 1

        aList[position] = cur_val


nums = list(map(int, input().split()))
rev_sort(nums)

num = int(input())
top_nums = [str(item) for item in nums[0:num]]
print(f"{' '.join(top_nums)}")