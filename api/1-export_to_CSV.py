#!/usr/bin/python3
"""
Exporting the data from the api requests to the csv file
"""

python
import requests
import csv
import sys

def get_employee_details(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()

def get_employee_todos(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()

def export_to_csv(employee_id, employee_details, employee_todos):
    file_name = f"{employee_id}.csv"
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in employee_todos:
            writer.writerow([employee_id, employee_details["username"], todo["completed"], todo["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_details = get_employee_details(employee_id)
    employee_todos = get_employee_todos(employee_id)
    export_to_csv(employee_id, employee_details, employee_todos)








