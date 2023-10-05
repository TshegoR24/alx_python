#!/usr/bin/python3
"""
Exporting the data from the api requests to the csv file
"""

import csv
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
# Create a CSV file
with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
    # Create a CSV writer
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    # Write the data rows
    for todo in todos:
        csvwriter.writerow([employee_id, employee_name, todo["completed"], todo["title"]])
