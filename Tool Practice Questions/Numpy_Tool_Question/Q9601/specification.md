# **Smart Electricity Consumption Analyzer**

## **Question Code: Q9601**

**Difficulty Level:** Medium
**Technology:** NumPy
**Total Marks:** 20
**Assessment SOP:** Independent test setup, latest-only report, no final score print

## **Assessment Instructions**
Open the Learnlytica assessment tool. Enter your Email address and Question ID, then click **Start Assessment**. Open VSCode and implement only in `solution.py`. After coding, click **Run Tests**, review the results, click **Validate**, and once satisfied click **Submit** and **End Assessment**.

> Sample inputs and expected outputs are illustrative only and are intentionally different from actual visible and hidden test data.

# **Problem Statement**
A smart-meter platform records the electricity consumed by a home on consecutive days. Each value represents daily consumption in kWh. Build a NumPy analyzer that prepares usage data, measures day-to-day change, identifies peak-use days, normalizes usage, and calculates short moving averages.

# **Class Creation**
```python
class ElectricityUsageAnalyzer:
```
No constructor is required.

## **1. Create Usage Array**
```python
def create_usage_array(self, readings: list) -> np.ndarray:
```
Convert the input into a NumPy array with `dtype=float`. Preserve order.

Example: `create_usage_array([8, 12.5, 10])` -> `array([8. , 12.5, 10. ])`

## **2. Validate Usage Array**
```python
def validate_usage_array(self, arr: np.ndarray) -> bool:
```
Return `False` for an empty array or if any value is negative. Otherwise return `True`.

## **3. Daily Usage Change**
```python
def daily_usage_change(self, arr: np.ndarray) -> np.ndarray:
```
Return the change from each day to the next using consecutive values. For `[10, 13, 11, 15]`, return `[3, -2, 4]` as a NumPy array. A one-element array should return an empty NumPy array.

## **4. Peak Usage Day Indices**
```python
def peak_usage_indices(self, arr: np.ndarray, threshold: float) -> np.ndarray:
```
Return the zero-based indices of days whose usage is **strictly greater than** `threshold`.

Example: `[8, 15, 20, 10]`, threshold `12` -> `array([1, 2])`.

## **5. Normalize Usage**
```python
def normalize_usage(self, arr: np.ndarray) -> np.ndarray:
```
Scale values to the range 0 to 1 using `(value - minimum) / (maximum - minimum)`. If all values are equal, return an array of zeros with the same shape. Round results to 3 decimals.

## **6. Three-Day Moving Average**
```python
def three_day_moving_average(self, arr: np.ndarray) -> np.ndarray:
```
Return the average for each consecutive window of 3 values. Round to 2 decimals. If fewer than 3 values are provided, return an empty NumPy array.

Example: `[6, 9, 12, 15]` -> `array([9., 12.])`.
