#!/usr/bin/python3
"""
Fetches and displays the to-do list details for a specified employee ID.

This script accepts an employee ID as a command-line argument, retrieves
the associated user data and to-do list from the JSONPlaceholder API,
and outputs the completed tasks for that employee.
"""


import re
import requests
import sys


REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])

            # Get the employee information
            user_url = f'{REST_API}/users/{employee_id}'
            user_response = requests.get(user_url).json()

            # Get the to-do list for the employee
            todos_url = f'{REST_API}/todos'
            todos_response = requests.get(todos_url).json()

            # Extract the employee's name
            employee_name = user_response.get('name')

            # Filter tasks for the specific employee
            tasks = list(filter(
                        lambda x: x.get(
                                'userId') == employee_id, todos_response))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            # Print the employee's name and the number of completed tasks
            print(f"Employee {employee_name} is done with tasks(
                                    {len(completed_tasks)}/{len(tasks)}): ")

            # Print each completed task
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print(f"\t {task.get('title')}")
        else:
            print("Please provide a valid employee ID.")
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
