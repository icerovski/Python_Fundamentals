# 02. Travel Company

line = input()
capacity_dict = {}
group_dict = {}

while not line == "ready":
    name = line.split(':')[0]
    raw_data = line.split(":")[1].replace(',',"-").split("-")

    vehicle_type = raw_data[0::2]
    capacity = raw_data[1::2]
    pairs = dict(zip(vehicle_type, capacity))

    if name not in capacity_dict.keys():
        capacity_dict[name] = pairs
    else:
        for key in pairs.keys():
            capacity_dict[name][key] = pairs[key]

    line = input()

line = input()
while not line == "travel time!":
    group_city = line.split()[0]
    group_size = line.split()[1]
    pairs = {group_city, group_size}

    if group_city not in group_dict.keys():
        group_dict[group_city] = group_size
    else:
        group_dict[group_city] += group_size

    line = input()

for name in group_dict.keys():
    transport_capacity = sum(int(capacity_dict[name][item]) for item in capacity_dict[name])
    people_count = int(group_dict[name])

    if transport_capacity >= people_count:
        print(f"{name} -> all {people_count} accommodated")
    else:
        print(f"{name} -> all except {people_count - transport_capacity} accommodated")