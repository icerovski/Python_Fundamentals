# Homework 02

list_strings = input().split(' ') # deletes all spaces, and returns a list
list_numbers = []

for n in list_strings:
    list_numbers.append(int(n))

print(list_numbers)

print("\nNew Exercise")
def multiply(num, multiplier):
    result = num * multiplier
    return result

# N.B. List Comprehension example
list_nums = list(map(int, input().split()))
print(list_nums)
multiplied_list = [multiply(el, 4) for el in list_nums]
print(multiplied_list)

for num in list_nums:
    print(f'{num}', end=' ')

# print(' '.join(list_nums))
print(*list_nums)

