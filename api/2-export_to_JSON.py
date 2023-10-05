#!/usr/bin/python3

python
import requests
import json

def get_employee_tasks(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()

def export_to_json(employee_id, tasks):
    file_name = f"{employee_id}.json"
    with open(file_name, 'w') as file:
        json.dump(tasks, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    tasks = get_employee_tasks(employee_id)
    export_to_json(employee_id, tasks)