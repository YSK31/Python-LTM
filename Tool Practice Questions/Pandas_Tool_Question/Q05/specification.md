# **Question Code: Q05**

Open the Learnlytica assessment tool.

Enter your Email address, then enter the Question ID and click **Start Assessment**.

Once the assessment starts, click on **VSCode**. The `solution.py` file will open directly. Write your code only in this file.

Once you have completed the code, return to the Learnlytica assessment tool and click **Run Tests**.

After executing the tests, click **Validate**.

Once validation is completed and you are satisfied with your attempt, click **Submit**, and then click **End Assessment**.

# **📌 Problem Statement**

You need to implement a Pandas-based **Sales List Manager** that operates entirely in memory using Python lists, dictionaries, and Pandas DataFrames.

The objective is to practice commonly used Pandas operations, including:

* DataFrame creation using `pd.DataFrame(data, columns=[...])`
* Numeric type conversion
* String cleanup using `str.strip()` and `str.title()`
* `groupby()` using two columns
* `merge()` using aggregated DataFrames
* Assigning High, Medium, and Low flags based on business rules
* Creating crosstabs
* Filtering using boolean conditions
* Aggregations
* `value_counts()`
* Missing-value handling
* Ranking using `nlargest()` and `nsmallest()`
* Date handling using `OrderDate`
* Month-based revenue grouping

No external CSV files are used.

The driver will create a list of 10 sales records along with a column list.

Your class must implement all **20 methods** described below.

# **📌 Class Declaration**

```python
class SalesListManager:
```

The `__init__` method is optional.

If used, it must contain only:

```python
def __init__(self):
    pass
```

Do not change the class name.

# **📌 Operations**

## **1. Create and Clean DataFrame**

**Function Prototype:**

```python
def create_dataframe(self, data: list[dict], columns: list[str]) -> "pd.DataFrame":
```

**Purpose:**

Create a Pandas DataFrame and perform numeric conversion, string cleanup, and date parsing.

**Columns:**

```python
[
    "OrderID",
    "CustomerName",
    "Category",
    "Region",
    "Units",
    "UnitPrice",
    "Discount",
    "Channel",
    "OrderDate"
]
```

**Expected Output:**

* `OrderID` and `Units` must use nullable integer type `Int64`.
* `UnitPrice` and `Discount` must be converted to numeric values.
* Invalid numeric values must be converted to `NaN`.
* `CustomerName` must be stripped of leading/trailing spaces and converted to title case.
* `Category`, `Region`, and `Channel` must be stripped of leading/trailing spaces.
* `OrderDate` must be converted to datetime.
* Valid dates may appear in different date formats.

**Implementation Flow:**

💡 Use `pd.DataFrame(data, columns=columns)` to create the DataFrame.

💡 Use `pd.to_numeric(..., errors="coerce")` for numeric columns.

💡 Convert `OrderID` and `Units` to nullable `Int64`.

💡 Use `.astype(str).str.strip()` for string cleanup.

💡 Use `.str.title()` for `CustomerName`.

💡 Parse `OrderDate` using:

```python
pd.to_datetime(..., errors="coerce", format="mixed")
```

💡 Return the cleaned DataFrame.

---

## **2. Get Customer Names (Cleaned)**

**Function Prototype:**

```python
def get_customer_names(self, df: "pd.DataFrame") -> list[str]:
```

**Purpose:**

Return all customer names from the cleaned DataFrame.

**Expected Output:**

A Python list containing customer names in title case without leading or trailing spaces.

---

## **3. Group Units by Region and Category**

**Function Prototype:**

```python
def groupby_region_category_units(self, df: "pd.DataFrame") -> "pd.DataFrame":
```

**Purpose:**

Calculate the total number of units sold for every combination of `Region` and `Category`.

**Expected Output:**

A DataFrame containing:

```python
["Region", "Category", "Units"]
```

`Units` must contain the summed units for each `(Region, Category)` combination.

---

## **4. Compute Revenue per Order**

**Function Prototype:**

```python
def compute_revenue(self, df: "pd.DataFrame") -> "pd.DataFrame":
```

**Purpose:**

Create a `Revenue` column for every order.

**Formula:**

```text
Revenue = Units * UnitPrice * (1 - Discount)
```

If `Discount` is missing, treat it as `0`.

If `UnitPrice` is missing, ensure that the final `Revenue` value does not remain `NaN`.

**Expected Output:**

A new DataFrame containing a `Revenue` column with no missing values.

---

## **5. Assign Amount Flag (High / Medium / Low)**

**Function Prototype:**

```python
def assign_amount_flag(self, df: "pd.DataFrame") -> "pd.DataFrame":
```

**Purpose:**

Classify each order according to its `Revenue`.

**Rules:**

```text
Revenue < 300            → Low
300 <= Revenue < 800     → Medium
Revenue >= 800           → High
```

**Expected Output:**

A DataFrame containing a new column:

```python
"AmountFlag"
```

---

## **6. Category–Region Crosstab**

**Function Prototype:**

```python
def build_category_region_crosstab(self, df: "pd.DataFrame") -> "pd.DataFrame":
```

**Purpose:**

Create a crosstab showing the number of orders for each Category and Region combination.

**Expected Output:**

Equivalent to:

```python
pd.crosstab(df["Category"], df["Region"])
```

---

## **7. Filter by Region and Minimum Units**

**Function Prototype:**

```python
def filter_by_region_min_units(
    self,
    df: "pd.DataFrame",
    region: str,
    min_units: int
) -> "pd.DataFrame":
```

**Purpose:**

Return orders from the specified region where the number of units is greater than or equal to the given minimum.

**Condition:**

```text
Region == region
AND
Units >= min_units
```

**Expected Output:**

Return the filtered DataFrame with its index reset starting from `0`.

---

## **8. Compute Region Unit Share Using Merge**

**Function Prototype:**

```python
def compute_region_unit_share(self, df: "pd.DataFrame") -> "pd.DataFrame":
```

**Purpose:**

Calculate the unit share of each Category within its Region.

**Expected Output Columns:**

```python
[
    "Region",
    "Category",
    "Units",
    "RegionUnits",
    "UnitShare"
]
```

**Implementation Flow:**

💡 Group by `Region` and `Category` to calculate category-wise units.

💡 Group by `Region` to calculate total units in each region.

💡 Rename the regional total column as `RegionUnits`.

💡 Merge both aggregated DataFrames using `Region`.

💡 Calculate:

```text
UnitShare = Units / RegionUnits
```

---

## **9. Total Units Sold**

**Function Prototype:**

```python
def total_units(self, df: "pd.DataFrame") -> int:
```

**Purpose:**

Return the total number of units sold across all orders.

**Expected Output:**

An integer value.

---

## **10. Average Unit Price**

**Function Prototype:**

```python
def average_unit_price(self, df: "pd.DataFrame") -> float:
```

**Purpose:**

Calculate the average value of `UnitPrice`.

Missing values must be ignored.

**Expected Output:**

A float value.

---

## **11. Top N Orders by Revenue**

**Function Prototype:**

```python
def top_n_orders_by_revenue(
    self,
    df: "pd.DataFrame",
    n: int
) -> "pd.DataFrame":
```

**Purpose:**

Return the top `n` orders having the highest Revenue.

**Implementation Flow:**

💡 Ensure the `Revenue` column exists.

💡 Use Revenue for ranking.

💡 Return the top `n` rows in descending Revenue order.

💡 Reset the index before returning.

---

## **12. Bottom N Orders by Revenue**

**Function Prototype:**

```python
def bottom_n_orders_by_revenue(
    self,
    df: "pd.DataFrame",
    n: int
) -> "pd.DataFrame":
```

**Purpose:**

Return the bottom `n` orders having the lowest Revenue.

**Implementation Flow:**

💡 Ensure the `Revenue` column exists.

💡 Return the bottom `n` rows in ascending Revenue order.

💡 Reset the index before returning.

---

## **13. Channel Counts**

**Function Prototype:**

```python
def channel_counts(self, df: "pd.DataFrame") -> "pd.Series":
```

**Purpose:**

Return the number of orders for each value in the `Channel` column.

**Expected Output:**

A Pandas Series containing the channel counts.

---

## **14. Fill Missing UnitPrice with Mean**

**Function Prototype:**

```python
def fill_missing_unitprice_with_mean(
    self,
    df: "pd.DataFrame"
) -> "pd.DataFrame":
```

**Purpose:**

Replace missing `UnitPrice` values using the mean of the available `UnitPrice` values.

**Expected Output:**

A new DataFrame where `UnitPrice` does not contain missing values.

---

## **15. Drop Rows with Missing Discount**

**Function Prototype:**

```python
def drop_rows_missing_discount(
    self,
    df: "pd.DataFrame"
) -> "pd.DataFrame":
```

**Purpose:**

Remove all rows where `Discount` is missing.

**Expected Output:**

Return the resulting DataFrame with its index reset starting from `0`.

---

## **16. Orders with Any Missing Values**

**Function Prototype:**

```python
def orders_with_missing_values(
    self,
    df: "pd.DataFrame"
) -> "pd.DataFrame":
```

**Purpose:**

Return all rows containing at least one missing value in any column.

**Implementation Flow:**

💡 Check all columns for missing values.

💡 Select rows where at least one value is missing.

💡 Reset the index before returning.

---

## **17. Filter by Channel and Amount Flag**

**Function Prototype:**

```python
def filter_by_channel_and_flag(
    self,
    df: "pd.DataFrame",
    channel: str,
    flag: str
) -> "pd.DataFrame":
```

**Purpose:**

Return orders matching both the specified `Channel` and `AmountFlag`.

**Condition:**

```text
Channel == channel
AND
AmountFlag == flag
```

**Implementation Flow:**

💡 Ensure `AmountFlag` exists before filtering.

💡 Apply both filtering conditions.

💡 Reset the index before returning.

---

## **18. Summary Stats for Units, UnitPrice, and Revenue**

**Function Prototype:**

```python
def summary_stats(self, df: "pd.DataFrame") -> "pd.DataFrame":
```

**Purpose:**

Calculate summary statistics for:

```python
["Units", "UnitPrice", "Revenue"]
```

**Expected Output:**

Return a DataFrame containing the following statistic rows:

```text
sum
mean
min
max
```

and the following columns:

```text
Units
UnitPrice
Revenue
```

**Implementation Flow:**

💡 Ensure the `Revenue` column exists using the same calculation used in `compute_revenue()`.

💡 Select:

```python
["Units", "UnitPrice", "Revenue"]
```

💡 Calculate:

```text
sum
mean
min
max
```

for each selected column.

💡 Return the resulting DataFrame.

---

## **19. Monthly Revenue (Year–Month Groupby)**

**Function Prototype:**

```python
def monthly_revenue(self, df: "pd.DataFrame") -> "pd.Series":
```

**Purpose:**

Calculate total Revenue grouped by year and month.

For example:

```text
2024-01
2024-02
2024-03
```

**Expected Output:**

A Pandas Series where:

* The index contains month values as `"YYYY-MM"` strings.
* The values contain total Revenue for each month.

**Implementation Flow:**

💡 Ensure the `Revenue` column exists using the same calculation used in `compute_revenue()`.

💡 Ensure `OrderDate` is converted to datetime.

💡 The input may contain valid dates in different formats.

💡 Parse dates using:

```python
pd.to_datetime(..., errors="coerce", format="mixed")
```

💡 Group Revenue using:

```python
OrderDate.dt.to_period("M")
```

💡 Sum Revenue for each month.

💡 Convert the resulting Period index to strings such as:

```text
2024-01
2024-02
```

💡 Return the resulting Pandas Series.

---

## **20. Add Discount Amount Column**

**Function Prototype:**

```python
def add_discount_amount_column(
    self,
    df: "pd.DataFrame"
) -> "pd.DataFrame":
```

**Purpose:**

Add a new column named:

```python
"DiscountAmount"
```

**Formula:**

```text
DiscountAmount = Units * UnitPrice * Discount
```

If `Discount` is missing, treat it as `0`.

If `UnitPrice` is missing, ensure the final `DiscountAmount` does not remain `NaN`.

**Expected Output:**

Return a new DataFrame containing the `DiscountAmount` column.

# **📌 Notes and Constraints**

* Import Pandas as:

```python
import pandas as pd
```

* Do not print anything inside the class methods.
* Do not read any files inside `solution.py`.
* Do not write any files inside `solution.py`.
* Use Pandas operations instead of Python loops wherever possible.
* Do not change the class name.
* Do not change any function name.
* Do not change parameter names.
* Do not change function signatures.
* Each method should return the required output.
* Methods that require `Revenue` or `AmountFlag` should work correctly even if those columns are not already present in the supplied DataFrame.
