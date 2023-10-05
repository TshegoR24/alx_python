#!/usr/bin/python3

import json
import requests
import sys
# Get the employee ID from the command line
employee_id = sys.argv[1]
# Get the employee's TODO list
response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
todos = response.json()
# Get the employee's name
response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
employee = response.json()
# Create a dictionary of the employee's TODO list
employee_todos = {}
employee_todos[employee["id"]] = []
# Add each TODO to the dictionary
for todo in todos:
    employee_todos[employee["id"]].append({"task": todo["title"], "completed": todo["completed"], "username": employee["username"]})
# Write the dictionary to a JSON file
with open("{}.json".format(employee_id), "w") as jsonfile:
    json.dump(employee_todos, jsonfile)