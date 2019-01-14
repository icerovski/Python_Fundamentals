print("\nNew Exercise")

list_numbers = [1, 2, 3, 4, 5, 6, 7]

print(list_numbers[0:3])

print(max(list_numbers))


print("\nNew Exercise")

list_1 = [10, 1, 2, 3, 4, 5, 6, 7]
list_2 = [100, 2000]

list_1.append(3000)
print(list_1)

list_1.extend(list_2)
print(list_1)

print("\nNew Exercise")
list_a = [1, 2, 3]
list_a.insert(2, 10)
print(list_a)

# N.B. pop gets an index, remove gets an item in the list

print("\nNew Exercise")
list_b = [1, 2, 3]
print(list_b.reverse())
list_b.reverse()
print(list_b)

a = reversed(list_b)
print(list_b)