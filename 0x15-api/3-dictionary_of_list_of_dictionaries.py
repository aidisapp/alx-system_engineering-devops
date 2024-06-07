#!/usr/bin/python3
"""
This script exports data of tasks from all employees in JSON format.
The JSON format is: { "USER_ID": [ {"username": "USERNAME", "task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], ... }
The exported data is saved in a file named todo_all_employees.json.
"""

import json
import requests


def fetch_all_employee_data():
    """Fetch data of all employees from the placeholder API"""
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(url_users)
    todos_response = requests.get(url_todos)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        raise Exception("Failed to fetch data from the API")

    users = users_response.json()
    todos = todos_response.json()

    return users, todos


def export_all_to_json(users, todos):
    """Export data of all employees to a JSON file"""
    data = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        tasks = []
        for todo in todos:
            if todo['userId'] == user_id:
                task_dict = {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": username
                }
                tasks.append(task_dict)

        data[str(user_id)] = tasks

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)


def main():
    """Main function to handle the script execution"""
    try:
        users, todos = fetch_all_employee_data()
        export_all_to_json(users, todos)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
