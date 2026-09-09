Greenhouse Crop Production Analyzer
Question Code: Q9403
Difficulty Level	Medium
Technology	Pandas
Total Marks	20
Assessment SOP	Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.
Problem Statement
A greenhouse tracks daily crop production logs with PlotID, Date, YieldKg, Temperature, and DowntimeMinutes. Build analytics to summarize yield, calculate efficiency, categorize temperature bands, filter downtime rows, and identify top production days.
Class Creation
class GreenhouseAnalyzer:
Constructor
def __init__(self):
    pass
Operations
1. Create Production DataFrame
Function Prototype
def create_production_df(self, data: list) -> pd.DataFrame:
Example Input
analyzer.create_production_df([["P1", "2025-05-01", 120.0, 24.5, 20], ["P2", "2025-05-01", 90.0, 31.0, 0]])
Expected Output
Columns: PlotID, Date, YieldKg, Temperature, DowntimeMinutes
Implementation Flow
•	Create a DataFrame using columns ["PlotID", "Date", "YieldKg", "Temperature", "DowntimeMinutes"].
•	Keep Date as string.
•	Return the DataFrame.
2. Total Yield per Plot
Function Prototype
def total_yield_per_plot(self, df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.total_yield_per_plot(df)
Expected Output
Columns: PlotID, TotalYield
Implementation Flow
•	Group by PlotID.
•	Sum YieldKg.
•	Use reset_index().
•	Rename YieldKg to TotalYield.
•	Return the DataFrame.
3. Add Yield per Active Minute
Function Prototype
def add_yield_per_active_min(self, df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.add_yield_per_active_min(df)
Expected Output
Adds YieldPerMin column
Implementation Flow
•	Assume one day has 1440 minutes.
•	Calculate active minutes as 1440 - DowntimeMinutes.
•	Calculate YieldPerMin = YieldKg / active minutes.
•	Round YieldPerMin to 2 decimals.
•	Return updated DataFrame.
4. Categorize Temperature Band
Function Prototype
def categorize_temperature_band(self, df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.categorize_temperature_band(df)
Expected Output
Adds TempBand column
Implementation Flow
•	Create default column TempBand = "Cool".
•	Use .loc to set TempBand to "Warm" where Temperature >= 20.
•	Use .loc to set TempBand to "Hot" where Temperature >= 30.
•	Return updated DataFrame.
Hidden Test Focus
•	Boundary: 19.9 Cool, 20.0 Warm, 29.9 Warm, 30.0 Hot.
5. Frequent Downtime Rows
Function Prototype
def frequent_downtime_rows(self, df: pd.DataFrame, n: int) -> pd.DataFrame:
Example Input
analyzer.frequent_downtime_rows(df, 15)
Expected Output
Rows where DowntimeMinutes > 15
Implementation Flow
•	Filter rows where DowntimeMinutes is strictly greater than n.
•	Return the filtered DataFrame.
Hidden Test Focus
•	Threshold comparison must be strict greater than.
6. Clean and Top Yield Days
Function Prototype
def clean_and_top_yield_days(self, df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.clean_and_top_yield_days(df)
Expected Output
Cleaned rows sorted by YieldKg descending
Implementation Flow
•	Use dropna() to remove rows containing null values.
•	Sort by YieldKg in descending order using sort_values().
•	Reset index if needed for clean output.
•	Return the cleaned and sorted DataFrame.
Driver and SOP Notes
Assessment behavior:
•	Each test case has its own setup data; no function depends on another function passing.
•	The driver overwrites test_report.log on every execution using latest run data only.
•	The report lists individual pass/fail/crash results and error details only.
•	No total score, marks obtained, final score, or percentage is printed at the end.
