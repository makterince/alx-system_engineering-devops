#!/usr/bin/python3
""" scripts returns info about emplyee """
import requests

def get_employee_details(employee_id):
    """ make api request """
    response = request.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')

    if response.status_code == 200:
        todos = response.json()

        completed_tasks = [todo for todo in todos if todo['completed']]
        total_tasks = len(todos)
        num_completed_tasks = len(completed_tasks)

        employee_name = todos[0]['username']

        print(f'Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):')

        for task in completed_tasks:
            print("\t", task['title'])
    else:
        print(f"Error: {response.status_code}")

employee_id = int(input("Enter the employee ID: "))
get_employee_todo_progress(employee_id)
