Employee Shift Attendance Analyzer

**Question Code:**: Q9503

**Difficulty Level**: Medium

**Technology**: Pandas

**Total Marks**: 20

**Assessment SOP**: Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.

## Problem Statement

A manufacturing unit tracks employee shift attendance. Each record contains employee ID, department, shift date, attendance status, and overtime hours. Build an analyzer that prepares the data, standardizes dates, assigns attendance points, creates departmental summaries, filters overtime records, and creates a status count table.

## Class Creation

class ShiftAttendanceAnalyzer:

## Constructor

def __init__(self):
 pass

## Operations

1. Create Attendance DataFrame

Function Prototype
def create_attendance_df(self, data: list) -> pd.DataFrame:
Input rows contain [EmployeeID, Department, ShiftDate, Status, OvertimeHours].
Return columns EmployeeID, Department, ShiftDate, Status, OvertimeHours in the same input row order.

2. Standardize Shift Date

Function Prototype
def standardize_shift_date(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Return a copy of the DataFrame with ShiftDate converted to Pandas datetime values.
Do not change any other column or row order.

3. Add Attendance Points

Function Prototype
def add_attendance_points(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Add a column named AttendancePoints using these rules:
Present = 2
Leave = 1
Absent = 0
Return all existing columns plus AttendancePoints.

4. Department Attendance Summary

Function Prototype
def department_attendance_summary(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Return one row per Department with:
Department, TotalRecords, PresentCount, TotalOvertimeHours
TotalRecords is the number of attendance rows.
PresentCount counts rows whose Status is "Present".
TotalOvertimeHours is the sum of OvertimeHours.
Sort Department ascending and use a fresh 0-based index.

5. Filter Overtime Records

Function Prototype
def filter_overtime_records(self, df: pd.DataFrame, hours: float) -> pd.DataFrame:
Requirement
Return only rows where OvertimeHours is greater than or equal to hours.
Sort the selected rows by OvertimeHours descending. For equal overtime values, sort EmployeeID ascending.
Use a fresh 0-based index.

6. Department Status Table

Function Prototype
def department_status_table(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Return a table containing the count of Present, Absent, and Leave records for every Department.
Output columns must be exactly:
Department, Present, Absent, Leave
If a department does not contain one of the three statuses, its count must be

0.
Sort Department ascending and use a fresh 0-based index.

## Driver and SOP Notes

• Each test case has its own setup data; no function depends on another function passing.
• The driver overwrites test_report.log on every execution using latest run data only.
• The report lists individual pass/fail/crash results and error details only.
• No total score, marks obtained, final score, or percentage is printed at the end.
