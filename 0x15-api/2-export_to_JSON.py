#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress.
It uses a REST API to fetch the data and displays it on the standard output.
"""
if __name__ == "__main__":
    import requests
    import sys
    import json
    
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    
    res = requests.get("{}/{}".format(url, employee_id))
    employee_name = res.json().get("name")
    
    res = requests.get("{}/{}/todos".format(url, employee_id))
    tasks = res.json()
    
    task_details = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "name": employee_name}
        for task in tasks
    ]
    task_dict = {employee_id: task_details}

    file_name = "{}.json".format(employee_id)
    with open(file_name, "w", newline="") as f:
        json.dump(task_dict, f)
