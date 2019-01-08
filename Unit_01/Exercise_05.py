# 5. Numbers with Step

def get_input():
    start = int(input())
    end = int(input())
    step = int(input())
    return start, end, step

def print_output():
    start, end, step = get_input()
    for i in range(start, end, step):
        print(i)

print_output()