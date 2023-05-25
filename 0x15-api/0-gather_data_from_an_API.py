#!/usr/bin/python3
import request

def employee_details(employee_id):
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
            print(f"Employee {employee_name}
		  is done with tasks({done_tasks}/{total_tasks}):")

	    for task in completed_tasks:
           	 print(f"\t{task['title']}")
        
        except requests.exceptions.RequestException as e:
	        print(f"An error occurred: {e}")

employee_id = int(input("Enter the employee ID: "))
get_employee_todo_progress(employee_id)
