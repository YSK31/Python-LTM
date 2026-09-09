Public Library Borrowing Analyzer
Question Code: Q9501
Difficulty Level	Medium
Technology	Pandas
Total Marks	20
Assessment SOP	Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.

Problem Statement
A city library records book-borrowing activity. Each record contains a member ID, book category, borrow date, return date, and late fee. Build a Pandas-based analyzer that prepares the data, cleans invalid fee values, calculates borrowing duration, summarizes member activity, filters long borrowings, and identifies the highest-fee members.

Class Creation
class LibraryBorrowingAnalyzer:

Constructor
def __init__(self):
    pass

Operations

1. Create Borrowing DataFrame
Function Prototype
def create_borrowing_df(self, data: list) -> pd.DataFrame:

Input Format
Each inner list contains:
[MemberID, Category, BorrowDate, ReturnDate, LateFee]

Example Input
analyzer.create_borrowing_df([
    ["M201", "History", "2026-07-01", "2026-07-08", 0],
    ["M202", "Science", "2026-07-03", "2026-07-20", 25]
])

Expected Output
A DataFrame with columns in this exact order:
MemberID, Category, BorrowDate, ReturnDate, LateFee
The input row order must remain unchanged.

2. Clean Late Fee Values
Function Prototype
def clean_late_fees(self, df: pd.DataFrame) -> pd.DataFrame:

Requirement
Return a copy of the DataFrame where missing LateFee values are replaced with 0 and negative LateFee values are also changed to 0.
All other values and rows must remain unchanged.

3. Add Borrowing Days
Function Prototype
def add_borrowing_days(self, df: pd.DataFrame) -> pd.DataFrame:

Requirement
Convert BorrowDate and ReturnDate to Pandas datetime values and add a new column named BorrowingDays.
BorrowingDays must contain the number of calendar days between ReturnDate and BorrowDate.
Return all original columns plus BorrowingDays.

4. Member Borrowing Summary
Function Prototype
def member_borrowing_summary(self, df: pd.DataFrame) -> pd.DataFrame:

Requirement
Return one row per MemberID with these columns:
MemberID, BooksBorrowed, TotalLateFee
BooksBorrowed is the number of borrowing records for that member.
TotalLateFee is the sum of LateFee for that member.
Sort the final result by MemberID in ascending order and use a fresh 0-based index.

5. Filter Long Borrowings
Function Prototype
def filter_long_borrowings(self, df: pd.DataFrame, days: int) -> pd.DataFrame:

Requirement
Return only rows where BorrowingDays is strictly greater than days.
Keep the existing column order and preserve the original DataFrame index.

6. Top Members by Late Fee
Function Prototype
def top_members_by_fee(self, df: pd.DataFrame, n: int) -> pd.DataFrame:

Requirement
Return the top n members based on total LateFee.
The output columns must be:
MemberID, TotalLateFee
Sort TotalLateFee from highest to lowest. If two members have the same TotalLateFee, sort MemberID in ascending order.
Use a fresh 0-based index.

Driver and SOP Notes
• Each test case has its own setup data; no function depends on another function passing.
• The driver overwrites test_report.log on every execution using latest run data only.
• The report lists individual pass/fail/crash results and error details only.
• No total score, marks obtained, final score, or percentage is printed at the end.
