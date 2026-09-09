Warehouse Inventory Movement Analyzer
Question Code: Q9502
Difficulty Level	Medium
Technology	Pandas
Total Marks	20
Assessment SOP	Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.

Problem Statement
A warehouse maintains a product master and daily stock-movement records. Build a Pandas analyzer that creates both datasets, combines product details with movements, calculates movement value, summarizes category activity, and finds products with high outbound quantity.

Class Creation
class InventoryMovementAnalyzer:

Constructor
def __init__(self):
    pass

Operations

1. Create Product DataFrame
Function Prototype
def create_product_df(self, data: list) -> pd.DataFrame:
Input rows contain [ProductID, ProductName, Category, UnitPrice].
Return a DataFrame with columns ProductID, ProductName, Category, UnitPrice in this exact order.

2. Create Movement DataFrame
Function Prototype
def create_movement_df(self, data: list) -> pd.DataFrame:
Input rows contain [MovementID, ProductID, MovementType, Quantity, MovementDate].
Return a DataFrame with columns MovementID, ProductID, MovementType, Quantity, MovementDate in this exact order.

3. Combine Product and Movement Data
Function Prototype
def merge_product_movements(self, products_df: pd.DataFrame, movements_df: pd.DataFrame) -> pd.DataFrame:
Requirement
Return all movement rows with the matching ProductName, Category, and UnitPrice added from the product data.
The output column order must be:
MovementID, ProductID, MovementType, Quantity, MovementDate, ProductName, Category, UnitPrice
Preserve the movement row order.

4. Add Movement Value
Function Prototype
def add_movement_value(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Add a column named MovementValue equal to Quantity multiplied by UnitPrice.
Return all existing columns plus MovementValue.

5. Category Movement Summary
Function Prototype
def category_movement_summary(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Return one row per Category with these columns:
Category, InQuantity, OutQuantity
InQuantity is the total Quantity where MovementType is "IN".
OutQuantity is the total Quantity where MovementType is "OUT".
A category with no IN or no OUT movements must show 0 for that quantity.
Sort Category ascending and use a fresh 0-based index.

6. High Outbound Products
Function Prototype
def high_outbound_products(self, df: pd.DataFrame, n: int) -> pd.DataFrame:
Requirement
Calculate total OUT quantity for each ProductID and ProductName.
Return only products whose total OUT quantity is strictly greater than n.
Output columns:
ProductID, ProductName, TotalOutQuantity
Sort TotalOutQuantity descending, then ProductID ascending for ties. Use a fresh 0-based index.

Driver and SOP Notes
• Each test case has its own setup data; no function depends on another function passing.
• The driver overwrites test_report.log on every execution using latest run data only.
• The report lists individual pass/fail/crash results and error details only.
• No total score, marks obtained, final score, or percentage is printed at the end.
