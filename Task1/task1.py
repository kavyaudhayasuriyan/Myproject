import csv


# Custom exception
class InvalidSalaryError(Exception):
    pass


# Bonus function
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


# Employee class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# Manager inherits Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"Name: {self.name}, Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )


# Employee data
employees = [
    {"id": 1, "name": "Arun", "department": "Sales",
     "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR",
     "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT",
     "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT",
     "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance",
     "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales",
     "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT",
     "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR",
     "salary": 48000, "city": "Mumbai"}
]


# Write employee data to CSV file
with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "name", "department", "salary", "city"]
    )
    writer.writeheader()
    writer.writerows(employees)


# Read employee data from CSV file
with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)


# List comprehension: salary above 50000
above_50000 = [
    emp["name"] for emp in data
    if int(emp["salary"]) > 50000
]
print("Above 50000:", above_50000)


# Filter: Chennai employees
chennai = list(filter(
    lambda emp: emp["city"] == "Chennai", data
))
print("Chennai:", [emp["name"] for emp in chennai])


# Map and lambda: add 10% raise
raised_salaries = list(map(
    lambda emp: int(emp["salary"]) * 1.10, data
))
print("Salaries after 10% raise:", raised_salaries)


# Bonus function example
print("Bonus:", bonus(30000, 0.1, 500, 1000, cap=4000))


# Employee and Manager examples
emp = Employee("Arun", 30000)
print("Annual Salary:", emp.annual_salary())

manager = Manager("Priya", 60000, 5)
print(manager.get_details())


# Exception handling
try:
    emp = Employee("Test", -500)
except InvalidSalaryError as error:
    print("Error:", error)
finally:
    print("Transaction finished")


# Loop: continue and break
salaries = [30000, 0, 45000, 60000, 90000, 52000]

for salary in salaries:
    if salary == 0:
        continue

    if salary > 85000:
        break

    print("Processed salary:", salary)
