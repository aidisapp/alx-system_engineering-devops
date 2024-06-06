#!/usr/bin/python3
"""
Fetches and displays the to-do list details for a specified employee ID.

This script accepts an employee ID as a command-line argument, retrieves
the associated user data and to-do list from the JSONPlaceholder API,
and outputs the completed tasks for that employee in the console and
exports all tasks data to a CSV file.
"""

import csv
import requests
import sys


API_ENDPOINT = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        user_url = f"{API_ENDPOINT}/users/{user_id}"
        user_response = requests.get(user_url)
        """ANYTHING"""
        user_data = user_response.json()
        user_name = user_data.get('username')

        todos_url = f"{user_url}/todos"
        todos_response = requests.get(todos_url)
        tasks = todos_response.json()

        # Print the completed tasks to the console
        completed_tasks = [task for task in tasks if task.get('completed')]
        print(f"Employee {user_data.get(
                        'name')} is done with tasks({len(
                                    completed_tasks)}/{len(tasks)}): ")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

        # Write tasks to a CSV file
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in tasks:
                completed = task.get('completed')
                """Complete"""
                title_task = task.get('title')
                """Done"""
                csv_writer.writerow(
                            [user_id, user_name, completed, title_task])
    else:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
