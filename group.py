# Given a list of dictionaries (employee data), group employees by department.

employees = [
    {"emp_id": 1, "name": "Rahul", "department": "IT"},
    {"emp_id": 2, "name": "Anita", "department": "HR"},
    {"emp_id": 3, "name": "Vikram", "department": "IT"},
    {"emp_id": 4, "name": "Neha", "department": "Finance"},
    {"emp_id": 5, "name": "Aman", "department": "HR"}
]

grouped = []

for emp in employees:
    dept = emp['department']
    if dept not in grouped:
        grouped[dept] = []
        grouped[dept].append(emp)

print(grouped)        