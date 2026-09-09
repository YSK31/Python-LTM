Retail Campaign Performance Dashboard
Question Code: Q9401
Difficulty Level	Medium
Technology	Pandas
Total Marks	20
Assessment SOP	Independent test setup, latest-only report, no final score print


Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.
Problem Statement
A retail company tracks marketing campaign performance. Each record contains campaign name, channel, outcome, and leads generated. Build a dashboard to summarize leads, assign outcome points, filter high-lead records, compute conversion rate, and list top campaigns.
Class Creation
class CampaignDashboard:
Constructor
def __init__(self):
    pass
Operations
1. Create Campaign DataFrame
Function Prototype
def create_campaign_df(self, campaign_data: list) -> pd.DataFrame:
Example Input
analyzer.create_campaign_df([["Festive", "Email", "Converted", 45], ["Winter", "SMS", "Interested", 30]])
Expected Output
Columns: Campaign, Channel, Outcome, Leads
Implementation Flow
•	Create a DataFrame using columns ["Campaign", "Channel", "Outcome", "Leads"].
•	Do not modify or sort the input data.
•	Return the DataFrame.
2. Campaign Lead Summary
Function Prototype
def campaign_lead_summary(self, df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.campaign_lead_summary(df)
Expected Output
Columns: Campaign, Total Leads, Average Leads
Implementation Flow
•	Group by Campaign.
•	Aggregate Leads using sum and mean.
•	Rename output columns as "Total Leads" and "Average Leads".
•	Use reset_index().
•	Return only these three columns.
3. Add Outcome Points
Function Prototype
def add_outcome_points(self, df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.add_outcome_points(df)
Expected Output
Adds Points column
Implementation Flow
•	Create a dictionary mapping Converted to 5, Interested to 2, and Ignored to 0.
•	Use map() on Outcome column.
•	Store values in new column Points.
•	Return updated DataFrame.
4. Filter High Leads
Function Prototype
def filter_high_leads(self, df: pd.DataFrame, n: int) -> pd.DataFrame:
Example Input
analyzer.filter_high_leads(df, 40)
Expected Output
Rows where Leads > 40
Implementation Flow
•	Filter rows where Leads is strictly greater than n.
•	Return the filtered DataFrame without resetting index unless required by the driver output.
5. Compute Conversion Rate
Function Prototype
def compute_conversion_rate(self, df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.compute_conversion_rate(df)
Expected Output
Columns: Campaign, Conversion Rate
Implementation Flow
•	Group by Campaign and count total rows.
•	Filter rows where Outcome == "Converted" and count converted rows by Campaign.
•	Merge total and converted counts.
•	Use fillna(0) for campaigns with no conversions.
•	Calculate Conversion Rate = Converted / Total * 100.
•	Round to 1 decimal.
•	Return Campaign and Conversion Rate columns.
Hidden Test Focus
•	Campaigns with no Converted rows must return 0.0.
6. Top Campaigns by Points
Function Prototype
def top_campaigns_by_points(self, df: pd.DataFrame, n: int) -> pd.DataFrame:
Example Input
analyzer.top_campaigns_by_points(df, 2)
Expected Output
Columns: Campaign, Total Points
Implementation Flow
•	Group by Campaign and sum Points.
•	Rename Points to Total Points.
•	Sort by Total Points descending.
•	Use head(n).
•	Return the resulting DataFrame.
Hidden Test Focus
•	Sorting must be descending.
Driver and SOP Notes
Assessment behavior:
•	Each test case has its own setup data; no function depends on another function passing.
•	The driver overwrites test_report.log on every execution using latest run data only.
•	The report lists individual pass/fail/crash results and error details only.
•	No total score, marks obtained, final score, or percentage is printed at the end.
