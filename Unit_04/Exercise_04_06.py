# 06. Odd Numbers at Odd Positions

num_list = list(map(int, input().split(' ')))

for index in range(0, len(num_list)):
    if index % 2 == 1:
        if num_list[index] % 2 == abs(1):
            print(f"Index {index} -> {num_list[index]}")
