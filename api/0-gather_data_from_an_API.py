#!/usr/bin/python3

import requests
import sys
# Get the employee ID from the command line
employee_id = int(sys.argv[1])
# Get the employee's TODO list
response = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))
todos = response.json()
# Get the employee's name
response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
employee = response.json()
employee_name = employee["name"]
# Count the number of completed tasks
completed_tasks = 0
for todo in todos:
    if todo["completed"]:
        completed_tasks += 1
# Print the employee's TODO list progress
print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, len(todos)))
for todo in todos:
    if todo["completed"]:
        print("\t {}".format(todo["title"]))