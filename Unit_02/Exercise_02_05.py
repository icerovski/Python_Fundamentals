# 5. Calculate Triangle Area

def triangle_area(a, b):
    area = a * b / 2
    print(f'{area:.12g}')

a = float(input())
b = float(input())

triangle_area(a, b)
