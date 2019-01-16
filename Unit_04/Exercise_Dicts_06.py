# 06. Exam Shopping

inventory = {}


def stock_inventory():
    if product not in inventory:
        inventory[product] = quantity
    else:
        inventory[product] += quantity


def buy_inventory():
    if product not in inventory:
        print(f"{product} doesn't exist")
    elif inventory[product] == 0:
        print(f"{product} out of stock")
    else:
        inventory[product] = max(inventory[product] - quantity, 0)


def print_inventory():
    for key, value in inventory.items():
        if value <= 0:
            continue
        else:
            print(f'{key} -> {value}')


while True:
    line = input()
    if line == "exam time":
        print_inventory()
        break

    elif line == "shopping time":
        continue

    else:
        order = line.split(' ')
        order_type = order[0]
        product = order[1]
        quantity = int(order[2])

        if order_type == "stock":
            stock_inventory()
        elif order_type == "buy":
            buy_inventory()
