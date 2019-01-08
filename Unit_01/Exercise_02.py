# 2. Person Info
name = None
age = None
city = None
salary = None

def get_info():
    name = input()
    age = input()
    city = input()
    salary = float(input())
    return name, age, city, salary

def print_info():
    name, age, city, salary = get_info()
    print(f"{name} is {age} years old, is from {city} and makes ${salary}")

print_info()