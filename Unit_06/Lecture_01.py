nums = [1, 2, 3, 4, 5]

list_even_nums = list(filter(lambda x: x%2 == 0, nums)) # this function iterates through the whole list
print(list_even_nums)

other_list =[]
for num in nums:
    other_list.append(num+2)

print(nums)
print[other_list]