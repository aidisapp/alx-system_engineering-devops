#!/usr/bin/python3
"""
Fetches and displays the to-do list details for a specified employee ID.

This script accepts an employee ID as a command-line argument, retrieves
the associated user data and to-do list from the JSONPlaceholder API,
and outputs the completed tasks for that employee.
"""


import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get user information
    user_url = f"{base_url}users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Get TODO list for the user
    todos_url = f"{base_url}todos"
    params = {"userId": employee_id}
    todos_response = requests.get(todos_url, params=params)
    todos_data = todos_response.json()

    # Extracting employee name
    employee_name = user_data.get('name')

    # Extracting TODO information
    total_tasks = len(todos_data)
    completed_tasks = [task.get(
                        "title") for task in todos_data if task.get(
                                                                "completed")]

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks(
                            {len(completed_tasks)}/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid employee ID as an integer.")
