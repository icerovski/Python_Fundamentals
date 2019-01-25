# 04. List Contains Element

nums = list(map(int, input().split()))
the_num = int(input())
isFound = False

for el in nums:
    if el == the_num:
        isFound = True
        break

if isFound: print("yes")
else: print("no")