# 01. Sum Adjacent Equal Numbers

nums = list(map(float, input().split()))
i = 0

while i < len(nums) - 1:
    if nums[i] == nums[i+1]:
        del nums[i]
        nums[i] *= 2
        i = max(0, i - 1)
        continue
    i = max(0, i + 1)

print(f"{' '.join(map(lambda num: format(num, '.12g'), nums))}")