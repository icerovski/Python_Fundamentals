data = input()

city_dict = {}
trans_dict = {}

while data != 'ready':
    city = data.split(":")[0]
    transportation_list = data.split(":")[1].split(",")
    if city not in city_dict:
        city_dict.update({city: trans_dict})
        trans_dict = {}
        for items in transportation_list:
            vehicle = items.split("-")[0]
            vehicle_count = int(items.split("-")[1])
            city_dict[city].update({vehicle: vehicle_count})
    else:
        trans_dict = {}
        for items in transportation_list:
            vehicle = items.split("-")[0]
            vehicle_count = int(items.split("-")[1])
            city_dict[city].update({vehicle: vehicle_count})
    data = input()

data = input()

total = 0

while data != 'travel time!':
    city = data.split(" ")[0]
    passengers = int(data.split(" ")[1])
    for key, value in city_dict.items():
        if key == city:
            for key2, value2 in value.items():
                total += value2
    if total >= passengers:
        print(f'{city} -> all {passengers} accommodated')
    else:
        print(f'{city} -> all except {passengers - total} accommodated')
    total = 0
    data = input()