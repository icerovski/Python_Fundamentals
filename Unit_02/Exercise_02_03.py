# 3. Printing Triangle

def top_part(n):
    for row in range(1, n + 1):
        for col in range(1, row):
            print(f'{col}', end=' ')
        print()

def bottom_part(n):
    for row in range(n, 1, -1):
        for col in range(1, row):
            print(f'{col}', end=' ')
        print()

def middle_part(n):
    for col in range(1, n + 1):
        print(col, end=' ')
    print()

def print_triangle():
    top_part(num)
    middle_part(num)
    bottom_part(num)

num = int(input())
print_triangle()