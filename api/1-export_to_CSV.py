#!/usr/bin/python3

import requests
import csv
import sys

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Error: Could not fetch employee details")
        return

    employee_data = employee_response.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Fetch TODO list for the employee
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Could not fetch TODO list")
        return

    todos_data = todos_response.json()

    # Create and write to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            task_completed_status = "Completed" if todo["completed"] else "Not Completed"
            csv_writer.writerow([user_id, username, task_completed_status, todo["title"]])

    print(f"Data has been exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
