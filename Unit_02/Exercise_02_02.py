# 2. Sign of Integer Number

def define_sign(a):
    a = format_number(num)
    if a > 0:
        print(f"The number {a} is positive.")
    elif a == 0:
        print(f"The number {a} is zero.")
    else:
        print(f"The number {a} is negative.")

def format_number(b):
    if b % 1 == 0:
        return int(b)
    else:
        return b

num = float(input())
define_sign(num)