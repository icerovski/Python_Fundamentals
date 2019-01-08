# 3. Extended Person Info

def get_info():
    name = input()
    age = int(input())
    town = input()
    salary = float(input())
    return name, age, town, salary

def age_range(age):
    teen_cap = int(18)
    adult_cap = int(70)

    if age < teen_cap:
        age_label = "teen"
    elif age >= adult_cap:
        age_label = "elder"
    else:
        age_label = "adult"
    return age_label

def salary_range(salary):
    low_cap = float(500)
    medium_cap = float(2000)

    if salary < low_cap:
        salary_label = "low"
    elif salary >= medium_cap:
        salary_label = "high"
    else:
        salary_label = "medium"
    return salary_label

def print_info():
    name, age, town, salary = get_info()
    age_label = age_range(age)
    salary_label = salary_range(salary)
    print(f"Name: {name}\nAge: {age}\nTown: {town}\nSalary: ${salary:.2f}\nAge range: {age_label}\nSalary range: {salary_label}")

print_info()
