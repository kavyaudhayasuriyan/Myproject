
import csv
import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Read employees.csv
employees = []

with open("employees.csv", "r", newline="",encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["id"] = int(row["id"])
        row["salary"] = int(row["salary"])
        employees.append(row)

# Write employees.json
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

# Write high_earners.csv
high_earners = []

for employee in employees:
    if employee["salary"] > 50000:
        high_earners.append(employee)

with open("high_earners.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")

# GET users from API
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )
    response.raise_for_status()

    users = response.json()

    for user in users[:3]:
        print(f'{user.get("id")} - {user.get("name")} - {user.get("email")}')

    # Read a nested JSON field using get()
    first_user = users[0]
    address = first_user.get("address", {})
    city = address.get("city")

    result = {
        "id": first_user.get("id"),
        "name": first_user.get("name"),
        "city": city
    }

    with open("users.json", "w") as file:
        json.dump(result, file, indent=4)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

# Check a missing user
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)
