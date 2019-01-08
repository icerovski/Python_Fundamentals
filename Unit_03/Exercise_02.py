# 2. Person Info
name = None
age = None
city = None
salary = None

def get_info():
    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")
    salary = float(input("Salary: "))
    return name, age, city, salary

def print_info(a, b, c, d):
    a, b, c, d = get_info()
    print(f"{a}, is {b} old, is from {c} and makes ${d}.")

print_info(name, age, city, salary)