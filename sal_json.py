import os
import json
import csv

class Emplyee:  # Error: Typo in class name
    def __init__(self, emp_id, name, position, salary):  # Error: Wrong parameter name (emp_id should be employee_id)
        self.emp_id = emp_id  # Error: Wrong attribute name (self.emp_id should be self.employee_id)
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def to_dict(self):
        return {
            'employee_id': self.emp_id,  # Error: Wrong attribute name (self.emp_id should be self.employee_id)
            'name': self.name,
            'position': self.position,
            'salary': self.salary
        }

def read_employees_from_csv(file_path):
    employees = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                employee = Emplyee(  # Error: Typo in class name
                    emp_id=row['employee_id'],  # Error: Wrong parameter name (emp_id should be employee_id)
                    name=row['name'],
                    position=row['position'],
                    salary=float(row['salary'])
                )
                employees.append(employee)
            except ValueError as e:
                print(f"Skipping row due to error: {e} in {row}")
    return employees

def save_employees_to_json(employees, output_file):
    with open(output_file, 'w') as file:
        json.dump([employee.to_dict() for employee in employees], file, indent=4)

def main():  # Error: Missing indentation for this function
input_file = 'employees.csv'  # Error: Incorrect indentation
output_file = 'employees.json'  # Error: Incorrect indentation

    try:
        employees = read_employees_from_csv(input_file)  # Error: Incorrect indentation
        for employee in employees:
        employee.give_raise(5000)  # Error: Incorrect indentation
        save_employees_to_json(employees, output_file)  # Error: Incorrect indentation
        print(f"Employee data has been saved to {output_file}")  # Error: Incorrect indentation
    except Exception as e:
        print(f"An error occurred: {e}")  # Error: Incorrect indentation

if __name__ == "__main__":
    main()

