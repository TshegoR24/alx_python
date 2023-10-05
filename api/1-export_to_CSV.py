#!/usr/bin/python3
"""
Exporting the data from the api requests to the csv file
"""

python
import csv
import requests
from requests.auth import HTTPBasicAuth

# Replace with your own values
USERNAME = 'your_username'
PASSWORD = 'your_password'
USER_ID = 'your_user_id'

# Base URL for the Asana API
BASE_URL = 'https://app.asana.com/api/1.0'

# Get the user's tasks
def get_user_tasks(user_id):
    url = f'{BASE_URL}/users/{user_id}/tasks'
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    return response.json()['data']

# Write the tasks to a CSV file
def write_tasks_to_csv(tasks, user_id):
    file_name = f'{user_id}.csv'
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({'USER_ID': user_id, 'USERNAME': USERNAME, 'TASK_COMPLETED_STATUS': task['completed'], 'TASK_TITLE': task['name']})

# Main function
def main():
    tasks = get_user_tasks(USER_ID)
    write_tasks_to_csv(tasks, USER_ID)

if __name__ == '__main__':
    main()
