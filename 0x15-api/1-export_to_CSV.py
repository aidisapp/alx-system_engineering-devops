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
    USER = argv[1]
    USERNAME = API_ENDPOINT + '/users/' + USER
    res = requests.get(USERNAME)
    """ANYTHING"""
    user_name = res.json().get('username')
    TODO_URI = USERNAME + '/todos'
    res = requests.get(TODO_URI)
    tasks = res.json()

    with open('{}.csv'.format(USER), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                USER, user_name, completed, title_task))
