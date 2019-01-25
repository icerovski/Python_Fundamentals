# 06. Reverse List In-place

nums = input().split()
middle = len(nums) // 2 # use // for integer division

j = 0
for i in range(0, middle):
    j = j - 1
    nums[i], nums[j] = nums[j], nums[i]

print(f"{' '.join(nums)}")
