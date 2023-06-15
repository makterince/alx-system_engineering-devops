#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress.
It uses a REST API to fetch the data and displays it on the standard output.
"""
if __name__ == "__main__":
    import requests
    import sys
    import csv

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    
    res = requests.get("{}/{}".format(url, employee_id))
    employee_name = res.json().get("name")
    
    res = requests.get("{}/{}/todos".format(url, employee_id))
    tasks = res.json()

    file_name = "{}.csv".format(employee_id)
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks:
            row = [
                    employee_id, employee_name,
                    task["completed"], task["title"]
                    ]
            
            writer.writerow(row)
