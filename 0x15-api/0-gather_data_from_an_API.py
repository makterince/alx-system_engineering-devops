#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress.
It uses a REST API to fetch the data and displays it on the standard output.
"""
if __name__ == "__main__":
    import requests
    import sys

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get("{}/{}".format(url, employee_id))
    employee_name = res.json().get("name")

    res = requests.get("{}/{}/todos".format(url, employee_id))
    tasks = res.json()

    completed_tasks = [
            task.get("title")
            for task in tasks
            if task.get("completed")
    ]
    
    print("Employee {} is done with tasks({}/{}):"
            .format(employee_name, len(completed_tasks), len(tasks)))
    
    for task_name in completed_tasks:
        print("\t {}".format(task_name))
