# 02. Travel Company

capacity_dict = {}
group_dict = {}


line = input()
while not line == "ready":
    city = line.split(':')[0]
    raw_data = line.split(":")[1].split(",")
    vehicle_type = []
    capacity = []

    for items in raw_data:
        vehicle_type.append(items.split("-")[0])
        capacity.append(int(items.split("-")[1]))

        pairs = dict(zip(vehicle_type, capacity))

    if city not in capacity_dict.keys():
        capacity_dict[city] = pairs
    else:
        capacity_dict[city].update(pairs)

    #
    # vehicle_type = list(map(raw_data.split("-")[0::2]))
    # capacity = list(map(int, raw_data.split("-")[1::2]))
    # pairs = dict(zip(vehicle_type, capacity))
    #
    # if city not in capacity_dict.keys():
    #     capacity_dict[city] = pairs
    # else:
    #     for key in pairs.keys():
    #         capacity_dict[city][key] = pairs[key]

    line = input()

line = input()
while not line == "travel time!":
    group_city = line.split()[0]
    group_size = int(line.split()[1])
    # words = line.split()
    # group_city = " ".join(words[0:len(words)-1])
    # group_size = int(words[-1])

    if group_city not in group_dict.keys():
        group_dict[group_city] = group_size
    else:
        group_dict[group_city] += group_size

    line = input()


for city in group_dict.keys():
    transport_capacity = sum(capacity_dict[city][item] for item in capacity_dict[city])
    # transport_capacity = 0
    # for item in capacity_dict[city].values():
    #     transport_capacity += item
    people_count = int(group_dict[city])

    if transport_capacity < people_count:
        print(f"{city} -> all except {people_count - transport_capacity} accommodated")
    else:
        print(f"{city} -> all {people_count} accommodated")
