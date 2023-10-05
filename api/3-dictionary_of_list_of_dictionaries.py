#!/usr/bin/python3

import json
import requests
import sys
# Get all employees' TODO lists
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()
# Get all employees' names
response = requests.get("https://jsonplaceholder.typicode.com/users")
employees = response.json()
# Create a dictionary of all employees' TODO lists
all_todos = {}
for employee in employees:
    all_todos[employee["id"]] = []
# Add each employee's TODO list to the dictionary
for todo in todos:
    all_todos[todo["userId"]].append({"username": employee["username"], "task": todo["title"], "completed": todo["completed"]})
# Write the dictionary to a JSON file
with open("todo_all_employees.json", "w") as jsonfile:
    json.dump(all_todos, jsonfile)