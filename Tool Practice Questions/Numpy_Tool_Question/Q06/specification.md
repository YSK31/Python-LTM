# **NumPy Array Analysis**

## **Question Code: Q06**

## **Overview**

Implement the `NumpyArrayAnalyzer` class providing array utilities for orders and stock analyses plus general NumPy practice functions.

Two matrix-related functions and tests were intentionally removed for this assessment:

```python
reshape_to_matrix
transpose_matrix
```

Do not include top-level executable code in `solution.py`.

---

# **📌 Class Creation**

```python
class NumpyArrayAnalyzer:
```

---

# **📌 Order-Related Operations**

## **✅ 1. Create Order Array**

Creates a float NumPy array from the given order amounts.

### **Function Prototype**

```python
def create_order_array(self, amounts: List[float]) -> np.ndarray:
```

### **Implementation Flow**

* Create a float NumPy array from `amounts`.
* Return the created NumPy array.

---

## **✅ 2. Validate Order Array**

Checks whether the given order array contains valid order amounts.

### **Function Prototype**

```python
def validate_order_array(self, order_array: np.ndarray) -> bool:
```

### **Implementation Flow**

* Check whether `order_array` is non-empty.
* Ensure all values are `>= 0`.
* Return `True` if both conditions are satisfied.
* Otherwise, return `False`.

---

## **✅ 3. Apply Discount**

Applies a 10% discount to qualifying order amounts.

### **Function Prototype**

```python
def apply_discount(self, order_array: np.ndarray) -> np.ndarray:
```

### **Implementation Flow**

* Apply a 10% discount to elements `>= 150.0`.
* Keep the remaining values unchanged.
* Return the transformed array.

---

## **✅ 4. Format Order Amounts**

Formats order amounts as currency strings.

### **Function Prototype**

```python
def format_order_amounts(self, order_array: np.ndarray) -> np.ndarray:
```

### **Expected Format**

```text
"$100.00"
```

### **Implementation Flow**

* Format each order amount as currency.
* Use two decimal places.
* Return a `dtype=object` NumPy array of formatted strings.

---

## **✅ 5. Compute Order Summary**

Calculates the total, average, and maximum order amounts.

### **Function Prototype**

```python
def compute_order_summary(
    self,
    order_array: np.ndarray
) -> Tuple[float, float, float]:
```

### **Implementation Flow**

* Calculate the total order amount.
* Calculate the average order amount.
* Calculate the maximum order amount.
* Return:

```python
(total, average, max)
```

---

## **✅ 6. Flag High-Value Orders**

Labels orders as `"High"` or `"Normal"` according to the given threshold.

### **Function Prototype**

```python
def flag_high_value_orders(
    self,
    order_array: np.ndarray,
    threshold: float = 150.0
) -> np.ndarray:
```

### **Implementation Flow**

Apply the following rules:

```text
Value >= threshold  -> High
Value < threshold   -> Normal
```

Return the resulting NumPy label array.

---

# **📌 Stock-Related Operations**

## **✅ 1. Create Stock Array**

Creates a NumPy array from the given stock changes.

### **Function Prototype**

```python
def create_stock_array(self, changes: List[float]) -> np.ndarray:
```

### **Implementation Flow**

* Create a NumPy array from `changes`.
* Return the created NumPy array.

---

## **✅ 2. Validate Stock Array**

Checks whether the stock change values are within the expected range.

### **Function Prototype**

```python
def validate_stock_array(self, changes: np.ndarray) -> bool:
```

### **Implementation Flow**

* Validate the stock change values.
* Values are expected within:

```text
[-10, 10]
```

* Return `True` when the values are within the expected range.
* Otherwise, return `False`.

---

## **✅ 3. Compute Volatility**

Calculates the mean, standard deviation, and maximum stock change.

### **Function Prototype**

```python
def compute_volatility(
    self,
    changes: np.ndarray
) -> Tuple[float, float, float]:
```

### **Implementation Flow**

* Calculate the mean.
* Calculate the standard deviation.
* Calculate the maximum value.
* Use `ddof=1` for standard deviation when `n > 1`.
* Use `ddof=0` when the array contains only one value.
* Return:

```python
(mean, std, max)
```

---

## **✅ 4. Flag Volatile Stocks**

Classifies stock changes according to their risk category.

### **Function Prototype**

```python
def flag_volatile_stocks(self, changes: np.ndarray) -> np.ndarray:
```

### **Implementation Flow**

Apply the following categories:

```text
Value < 2         -> Stable
Value 2 to 5      -> Moderate Risk
Value > 5         -> High Risk
```

The range `2` to `5` is inclusive.

Return the resulting NumPy label array.

---

## **✅ 5. Longest Loss Streak**

Finds the longest consecutive negative-run length.

### **Function Prototype**

```python
def longest_loss_streak(self, changes: np.ndarray) -> int:
```

### **Implementation Flow**

* Identify consecutive negative stock changes.
* Track the length of each consecutive negative run.
* Return the longest consecutive negative-run length.

---

## **✅ 6. Format Stock Report**

Formats stock change values as percentage strings.

### **Function Prototype**

```python
def format_stock_report(self, changes: np.ndarray) -> np.ndarray:
```

### **Expected Format**

```text
"1.23%"
```

### **Implementation Flow**

* Format each stock change as a percentage string.
* Use two decimal places.
* Return the resulting NumPy array.

---

# **📌 Additional NumPy Practice Operations**

## **✅ 1. Create Sequential Array**

Creates a sequential NumPy array.

### **Function Prototype**

```python
def create_sequential_array(
    self,
    start: int,
    stop: int,
    step: int = 1
) -> np.ndarray:
```

### **Implementation Flow**

* Create a sequential array using `start`, `stop`, and `step`.
* The default value of `step` is `1`.
* Return the resulting NumPy array.

---

## **✅ 2. Compute Element-Wise Square**

Calculates the square of every element.

### **Function Prototype**

```python
def compute_elementwise_square(self, arr: np.ndarray) -> np.ndarray:
```

### **Implementation Flow**

* Calculate the square of each array element.
* Return the resulting NumPy array.

---

## **✅ 3. Compute Statistics**

Calculates basic statistics for the given array.

### **Function Prototype**

```python
def compute_statistics(
    self,
    arr: np.ndarray
) -> Tuple[float, float, float, float]:
```

### **Implementation Flow**

Calculate:

* Sum
* Mean
* Minimum
* Maximum

Return:

```python
(sum, mean, min, max)
```

---

## **✅ 4. Filter Above Threshold**

Filters values that are above the specified threshold.

### **Function Prototype**

```python
def filter_above_threshold(
    self,
    arr: np.ndarray,
    threshold: float
) -> np.ndarray:
```

### **Implementation Flow**

* Compare the array values with `threshold`.
* Keep values above the threshold.
* Return the filtered NumPy array.

---

## **✅ 5. Replace Negatives with Zero**

Replaces negative array values with zero.

### **Function Prototype**

```python
def replace_negatives_with_zero(self, arr: np.ndarray) -> np.ndarray:
```

### **Implementation Flow**

* Identify negative values.
* Replace negative values with `0`.
* Keep the remaining values unchanged.
* Return the resulting NumPy array.

---

## **✅ 6. Normalize Array**

Normalizes the array values to the range `[0,1]`.

### **Function Prototype**

```python
def normalize_array(self, arr: np.ndarray) -> np.ndarray:
```

### **Implementation Flow**

* Normalize the values to:

```text
[0,1]
```

* If all elements are equal, return a zeros array.
* Return the normalized NumPy array.

---

## **✅ 7. Concatenate Arrays**

Combines two NumPy arrays.

### **Function Prototype**

```python
def concatenate_arrays(
    self,
    a: np.ndarray,
    b: np.ndarray
) -> np.ndarray:
```

### **Implementation Flow**

* Concatenate arrays `a` and `b`.
* Return the resulting NumPy array.

---

## **✅ 8. Compute Dot Product**

Calculates the dot product of two arrays.

### **Function Prototype**

```python
def compute_dot_product(
    self,
    a: np.ndarray,
    b: np.ndarray
) -> float:
```

### **Implementation Flow**

* Calculate the dot product of arrays `a` and `b`.
* Return the resulting value.

---

## **✅ 9. Get Unique Values**

Returns the unique values present in the array.

### **Function Prototype**

```python
def get_unique_values(self, arr: np.ndarray) -> np.ndarray:
```

### **Implementation Flow**

* Find the unique values in `arr`.
* Return them as a NumPy array.

---

## **✅ 10. Sort Array**

Sorts the values in the given array.

### **Function Prototype**

```python
def sort_array(self, arr: np.ndarray) -> np.ndarray:
```

### **Implementation Flow**

* Sort the array values.
* Return the sorted NumPy array.

---

## **✅ 11. Count Non-Zero Values**

Counts the number of non-zero values in the array.

### **Function Prototype**

```python
def count_nonzero(self, arr: np.ndarray) -> int:
```

### **Implementation Flow**

* Count all values that are not equal to `0`.
* Return the count as an integer.

---

# **📌 Important Note**

Although tests will detect methods implemented as `pass` or returning constants, static checks are non-fatal.

If a method is detected as pass-only or constant-return, its corresponding visible test will be marked **Failed** with a clear reason indicating it was a placeholder.

---

# **📌 Static-Check Rules (Informational)**

* The grader looks for usage of `np.` tokens; missing tokens will be logged as warnings.
* Methods that do not reference their parameters may be flagged as suspicious (warning).

---

# **📌 Testing Behavior**

* Tests are deterministic (no hidden randomness).
* The driver writes results to `test_report.log`.
* Students should not change method names or signatures.

---

# **📌 Deliverables**

* `solution.py` containing the `NumpyArrayAnalyzer` class implementing required methods.
* `driver.py` (this file) will be used to grade students.
* `test_report.log` will be produced by the driver.
