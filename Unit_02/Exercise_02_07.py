# 7. Greater of Two Values

# def compare_int(a, b):
#     result = max(int(a), int(b))
#     # bo = type(result)
#     print(result)
#
# def compare_str(a, b):
#     result = max(a, b)
#     # bo = result.isdigit()
#     print(result)
#
# def type_choice(a, b):
#     if a.isdigit() and b.isdigit():
#         compare_int(a, b)
#     else:
#         compare_str(a, b)
#
# a = input()
# b = input()

def compare_int(a, b):
    result = max(int(a), int(b))
    print(result)

def compare_str(a, b):
    result = max(a, b)
    print(result)

def type_choice(type_input, a, b):
    if type_input == "int":
        compare_int(a, b)
    else:
        compare_str(a, b)

type_input = input()
a = input()
b = input()
type_choice(type_input, a, b)
