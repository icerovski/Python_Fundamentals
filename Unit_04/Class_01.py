# Creat a simple list
# In python one list can contain intiger, string, object, etc.

numbers_list = [1, 2, 3]
print(numbers_list[2])
print(numbers_list[-1])
print(numbers_list[-3])

# length of list

print(len(numbers_list))

# concatenate lists
numbers_list_2 = [4, 5, 6]
result = numbers_list + numbers_list_2
print(result)

# N.B. element in list
name = "My name"
print(name[2]) # 'space' is also a character

for letter in name:
    print(letter, end= '')

# numbers_list[0] *= 2 # change the value of index 0 to '2'

# N.B.
# for num in numbers_list: # this looks into collection ('1') and not in the index ([0])
for index in range(0, len(numbers_list)):
    numbers_list[index] = numbers_list[index] * 2
    print(numbers_list)


print("\nNew exercise")
list_1 = [1, 2] # in the memory it saves the ID for this list
list_2 = [3, 4] # in memory different ID
print(id(list_1))
print(id(list_2))


list_1 = list_2 # this gives the same ID for the two lists. This is valid for 'reference type of data'.
list_1.append(5) # this also changes list_2
print(list_1)
print(list_2)

print(id(list_1))
print(id(list_2))

# this is not valid for strings, because they are immutable.




