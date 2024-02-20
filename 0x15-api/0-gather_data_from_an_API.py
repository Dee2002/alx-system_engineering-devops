#!/usr/bin/python3
import requests
from sys import argv


def gather_data(employee_id):
    """
    Retrieves and displays TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.
    format(employee_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("Employee not found")
        return

    employee_name = todos[0]['username']
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, completed_tasks, total_tasks))
    for todo in todos:
        if todo['completed']:
            print("\t", todo['title'])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(argv[1])
        gather_data(employee_id)
