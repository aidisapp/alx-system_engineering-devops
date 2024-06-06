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


if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    """ANYTHING"""
    user_name = res.json().get('username')
    task = url_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
