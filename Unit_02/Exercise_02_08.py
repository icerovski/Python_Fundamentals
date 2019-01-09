# 08. Multiply Evens by Odds

def sum_even_digits(a, b):
    even_sum = 0
    for i in range(0, b):
        if int(a[i]) % 2 == 0:
            even_sum = even_sum + int(a[i])
    return even_sum

def sum_odd_digits(a, b):
    odd_sum = 0
    for i in range(0, b):
        if int(a[i]) % 2 != 0:
            odd_sum = odd_sum + int(a[i])
    return odd_sum

def multiply_digits(num):
    clean_num = ''.join(i for i in num if i.isdigit()) # strip all characters other than digits from the string
    length = int(len(clean_num)) # determine the length of the string

    even_sum = sum_even_digits(clean_num, length)
    odd_sum = sum_odd_digits(clean_num, length)

    result = even_sum * odd_sum
    print(result)

num = input()
multiply_digits(num)