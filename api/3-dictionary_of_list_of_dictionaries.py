#!/usr/bin/python3

python
import requests
import json

def get_all_tasks():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    return response.json()

def export_to_json(tasks):
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as file:
        json.dump(tasks, file)

def main():
    tasks = get_all_tasks()
    export_to_json(tasks)

if __name__ == "__main__":
    main()