#!/usr/bin/python3
"""
This script exports data of tasks owned by a given employee in JSON format.
The JSON format is: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...] }
The exported data is saved in a file named USER_ID.json.
"""

import json
import requests
import sys


def fetch_employee_data(user_id):
    """Fetch employee data from the placeholder API"""
    url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_response = requests.get(url_user)
    todos_response = requests.get(url_todos)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        raise Exception("Failed to fetch data from the API")

    user = user_response.json()
    todos = todos_response.json()

    return user, todos


def export_to_json(user, todos):
    """Export data to a JSON file"""
    user_id = user['id']
    username = user['username']

    tasks = []
    for todo in todos:
        task_dict = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        }
        tasks.append(task_dict)

    data = {str(user_id): tasks}

    with open(f"{user_id}.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)


def main():
    """Main function to handle the script execution"""
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py USER_ID")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user, todos = fetch_employee_data(user_id)
        export_to_json(user, todos)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
