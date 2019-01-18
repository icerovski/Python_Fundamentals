# 08. Filter Base

employees_age = {}
employees_salary = {}
employees_position = {}


def choose_db(val):
    if val == "Age":
        dict_print_db = employees_age
    elif val == "Salary":
        dict_print_db = employees_salary
    elif val == "Position":
        dict_print_db = employees_position
    return dict_print_db


def print_employees():
    stat = input()
    dict_print_db = choose_db(stat)
    separator = 20 * '='

    for key, value in dict_print_db.items():
        print(f'Name: {key}\n{stat}: {value}\n{separator}')

    return


while True:
    line = input().split(' -> ')
    if line[0] == 'filter base':
        print_employees()
        break
    else:
        name = line[0]
        employee_info = line[1]

        if employee_info.isdigit():
            employees_age[name] = employee_info
        else:
            try:
                employee_info = float(line[1])
                # a check for floats that are actually ment as integers and have a '.0' in the end, eg. 7.0, 1.0
                if employee_info % 1 == 0:
                    employee_info = int(employee_info)
                    employees_age[name] = employee_info
                else:
                    employees_salary[name] = employee_info
            except ValueError:
                employees_position[name] = employee_info
