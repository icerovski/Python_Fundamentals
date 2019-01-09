# 4. Draw a Filled Square

def dashed_line(n):
    for i in range(1, 2 * n + 1):
        print('-', end= '')

def mid_line(n):
    for x in range(1, 2 * n + 1):
        if x == 1 or x == 2 * n:
            print("-", end='')
        elif x % 2 == 0:
            print("\\", end='')
        else:
            print("/", end='')

def print_figure(n):
    for i in range(1, n + 1):
        if i == 1 or i == n:
            dashed_line(num)
        else:
            mid_line(num)
        print()

num = int(input())
print_figure(num)