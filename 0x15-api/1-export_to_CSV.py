#!/usr/bin/python3
"""
Fetches and exports the to-do list details for a specified
employee ID in CSV format.

This script accepts an employee ID as a command-line argument, retrieves
the associated user data and to-do list from the JSONPlaceholder API,
and exports the data to a CSV file.
The CSV format is: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
The exported data is saved in a file named USER_ID.csv.
"""

import csv
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


def export_to_csv(user, todos):
    """Export data to a CSV file"""
    user_id = user['id']
    username = user['username']

    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                    [user_id, username, todo['completed'], todo['title']])


def main():
    """Main function to handle the script execution"""
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py USER_ID")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user, todos = fetch_employee_data(user_id)
        export_to_csv(user, todos)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
