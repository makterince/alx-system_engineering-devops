#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress.
It uses a REST API to fetch the data and displays it on the standard output.
"""
import request

def employee_details(employee_id):
    """
        Retrieves and displays information about an employee's TODO list.
        Args:
            employee_id (int): The ID of the employee.
        Returns:
            None.
    """
    base_url = "https;//jsonplaceholder.typicode.com"
    employee_url =  f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    
    try:
        employee_response = request.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()
        
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        completed_tasks = [task for task in todos_data if task['completed']]
        employee_name = employee_data['name']
        total_tasks = len(todos_data)
        done_tasks = len(completed_tasks)
        print(f"Employee {employee_name}"
                "is done with tasks({done_tasks}/{total_tasks}):")
        
        for task in completed_tasks:
            print(f"\t{task['title']}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
