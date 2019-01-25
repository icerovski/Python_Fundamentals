# 03. Count Numbers

nums = list(map(int, input().split()))

for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):

        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

i = -1
j = -1
count = 1
while i < len(nums):
    i = i + 1
    j = i + 1
    if j < len(nums):
        if nums[i] == nums[j]:
            count += 1
            continue
    else:
        print(f"{nums[i]} -> {count}")
        break

    print(f"{nums[i]} -> {count}")
    count = 1
