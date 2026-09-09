Food Delivery Refund Analysis
Question Code: Q9402
Difficulty Level	Medium
Technology	Pandas
Total Marks	20
Assessment SOP	Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.
Problem Statement
A food delivery platform tracks orders and refund requests. Build DataFrames, merge orders with refunds, compute cuisine-level refund rate, identify high-refund restaurants, and clean invalid refund records.
Class Creation
class FoodRefundAnalyzer:
Constructor
def __init__(self):
    pass
Operations
1. Create Orders DataFrame
Function Prototype
def create_orders_df(self, order_data: list) -> pd.DataFrame:
Example Input
analyzer.create_orders_df([[11, "R101", "Italian", "2025-04-01", 650.0], [12, "R102", "Indian", "2025-04-02", 420.0]])
Expected Output
Columns: OrderID, RestaurantID, Cuisine, OrderDate, OrderAmount
Implementation Flow
•	Create a DataFrame using columns ["OrderID", "RestaurantID", "Cuisine", "OrderDate", "OrderAmount"].
•	Keep OrderDate as string.
•	Return the DataFrame.
2. Create Refunds DataFrame
Function Prototype
def create_refunds_df(self, refund_data: list) -> pd.DataFrame:
Example Input
analyzer.create_refunds_df([[11, "2025-04-03", 650.0, "Missing Item"]])
Expected Output
Columns: OrderID, RefundDate, RefundAmount, Reason
Implementation Flow
•	Create a DataFrame using columns ["OrderID", "RefundDate", "RefundAmount", "Reason"].
•	Return the DataFrame.
3. Merge Orders Refunds
Function Prototype
def merge_orders_refunds(self, orders_df: pd.DataFrame, refunds_df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.merge_orders_refunds(orders_df, refunds_df)
Expected Output
Merged DataFrame retaining all orders
Implementation Flow
•	Use pd.merge().
•	Merge on OrderID.
•	Use how="left" to keep all orders.
•	Return merged DataFrame.
4. Cuisine Refund Rate
Function Prototype
def cuisine_refund_rate(self, merged_df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.cuisine_refund_rate(merged_df)
Expected Output
Columns: Cuisine, Orders, ReturnedOrders, RefundRate
Implementation Flow
•	Group by Cuisine and count total orders using size().
•	Identify returned rows where RefundAmount is not null using notna().
•	Count returned orders by Cuisine.
•	Merge counts and fill missing returned counts with 0.
•	Calculate RefundRate = ReturnedOrders / Orders * 100.
•	Sort by Cuisine and reset index.
•	Return required columns.
5. High Refund Restaurants
Function Prototype
def high_refund_restaurants(self, merged_df: pd.DataFrame, n: int) -> pd.DataFrame:
Example Input
analyzer.high_refund_restaurants(merged_df, 1)
Expected Output
Columns: RestaurantID, ReturnCount
Implementation Flow
•	Consider only rows where RefundAmount is not null.
•	Group by RestaurantID and count rows using size().
•	Rename count column as ReturnCount.
•	Return only rows where ReturnCount > n.
•	Reset index with drop=True.
Hidden Test Focus
•	Threshold comparison must be strict greater than.
6. Clean Refunds Data
Function Prototype
def clean_refunds_data(self, refunds_df: pd.DataFrame) -> pd.DataFrame:
Example Input
analyzer.clean_refunds_data(refunds_df)
Expected Output
Valid rows with non-null Reason and RefundAmount > 0
Implementation Flow
•	Drop rows where Reason is null.
•	Keep rows where RefundAmount is not null and greater than 0.
•	Reset index with drop=True.
•	Return cleaned DataFrame.
Hidden Test Focus
•	Rows with null amount or null reason must be removed.
Driver and SOP Notes
Assessment behavior:
•	Each test case has its own setup data; no function depends on another function passing.
•	The driver overwrites test_report.log on every execution using latest run data only.
•	The report lists individual pass/fail/crash results and error details only.
•	No total score, marks obtained, final score, or percentage is printed at the end.
