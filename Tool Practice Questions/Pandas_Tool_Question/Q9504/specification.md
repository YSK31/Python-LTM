Digital Subscription Revenue Analyzer
Question Code: Q9504
Difficulty Level	Medium
Technology	Pandas
Total Marks	20
Assessment SOP	Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.

Problem Statement
A digital learning platform tracks subscription records. Each record contains subscriber ID, plan, start date, monthly fee, and subscription status. Build an analyzer that prepares and cleans the records, derives monthly revenue, summarizes plan performance, filters subscriptions by date, and identifies the highest-revenue plans.

Class Creation
class SubscriptionRevenueAnalyzer:

Constructor
def __init__(self):
    pass

Operations

1. Create Subscription DataFrame
Function Prototype
def create_subscription_df(self, data: list) -> pd.DataFrame:
Input rows contain [SubscriberID, Plan, StartDate, MonthlyFee, Status].
Return columns SubscriberID, Plan, StartDate, MonthlyFee, Status in this exact order.

2. Clean Subscription Data
Function Prototype
def clean_subscription_data(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Return a copy where rows with missing SubscriberID are removed.
Replace missing Plan values with "Unknown".
Replace missing MonthlyFee values with 0.
Use a fresh 0-based index.

3. Add Active Revenue
Function Prototype
def add_active_revenue(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Add ActiveRevenue.
For rows with Status equal to "Active", ActiveRevenue must equal MonthlyFee.
For every other status, ActiveRevenue must be 0.
Return all existing columns plus ActiveRevenue.

4. Plan Revenue Summary
Function Prototype
def plan_revenue_summary(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Return one row per Plan with:
Plan, Subscribers, ActiveSubscribers, TotalActiveRevenue
Subscribers is the number of rows for the plan.
ActiveSubscribers counts rows whose Status is "Active".
TotalActiveRevenue is the sum of ActiveRevenue.
Sort Plan ascending and use a fresh 0-based index.

5. Subscriptions Started On or After Date
Function Prototype
def subscriptions_from_date(self, df: pd.DataFrame, start_date: str) -> pd.DataFrame:
Requirement
Treat StartDate and start_date as dates.
Return subscriptions whose StartDate is on or after start_date.
Sort by StartDate ascending, then SubscriberID ascending. Use a fresh 0-based index.

6. Top Plans by Active Revenue
Function Prototype
def top_plans_by_revenue(self, df: pd.DataFrame, n: int) -> pd.DataFrame:
Requirement
Return the top n plans based on total ActiveRevenue.
Output columns:
Plan, TotalActiveRevenue
Sort revenue descending and Plan ascending for ties. Use a fresh 0-based index.

Driver and SOP Notes
• Each test case has its own setup data; no function depends on another function passing.
• The driver overwrites test_report.log on every execution using latest run data only.
• The report lists individual pass/fail/crash results and error details only.
• No total score, marks obtained, final score, or percentage is printed at the end.
