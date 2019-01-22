x_nums = list(map(float, input().split()))
y_nums = list(map(float, input().split()))


# points = []
# for index in range(0, len(x_nums)):
#     current = (x_nums[index], y_nums[index])
#     points.append()

points = list(zip(x_nums, y_nums))
print(points)
print(points[0][0])