Clinic Appointment Queue System
Question Code: Q9204
Difficulty Level	Easy
Technology	Python OOP
Total Marks	10
Assessment SOP	Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.
Problem Statement
A clinic tracks waiting patient counts for departments. Each department is stored as the key and waiting count as the value. The system should add departments, update waiting counts, identify crowded departments, and assign queue actions.
Class Creation
class ClinicQueueSystem:
Constructor
def __init__(self):
    self.queue_data = {}
Operations
1. Add Department
Function Prototype
def add_department(self, department: str, waiting_count: int) -> dict:
Example Input
system.add_department("Radiology", 14)
Expected Output
{"Radiology": 14}
Implementation Flow
•	Insert department as key and waiting_count as value in self.queue_data.
•	Return self.queue_data.
2. Update Waiting Count
Function Prototype
def update_waiting_count(self, department: str, new_count: int) -> dict:
Example Input
system.update_waiting_count("Radiology", 28)
Expected Output
{"Radiology": 28}
Implementation Flow
•	Check whether department exists in self.queue_data.
•	If missing, raise KeyError("Department not found").
•	Update the department count with new_count.
•	Return self.queue_data.
Hidden Test Focus
•	Missing department update must raise only KeyError("Department not found").
3. Crowded Departments
Function Prototype
def crowded_departments(self, threshold: int) -> dict:
Example Input
system.crowded_departments(30)
Expected Output
{"Ortho": 45, "Neuro": 52}
Implementation Flow
•	Declare an empty dictionary.
•	Iterate through self.queue_data using an explicit loop.
•	Include departments where waiting count is strictly greater than threshold.
•	Return the result dictionary.
4. Assign Queue Actions
Function Prototype
def assign_queue_actions(self) -> dict:
Example Input
system.assign_queue_actions()
Expected Output
{"General": "Fast Queue", "ENT": "Normal Queue", "Cardio": "Open Extra Counter"}
Implementation Flow
•	Declare an empty dictionary.
•	For each department count, assign action.
•	If count > 60, action is "Open Extra Counter".
•	If count is 25 to 60 inclusive, action is "Normal Queue".
•	Otherwise action is "Fast Queue".
•	Return the action dictionary.
Hidden Test Focus
•	Boundary: count 25 and 60 should be "Normal Queue"; count 61 should be "Open Extra Counter".
Driver and SOP Notes
Assessment behavior:
•	Each test case has its own setup data; no function depends on another function passing.
•	The driver overwrites test_report.log on every execution using latest run data only.
•	The report lists individual pass/fail/crash results and error details only.
•	No total score, marks obtained, final score, or percentage is printed at the end.
•	OOP questions are easy category with total 10 marks.
•	Only 2 hidden test cases are used; each hidden test validates one function only.
