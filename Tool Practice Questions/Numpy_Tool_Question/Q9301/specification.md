# **Video Streaming Watch-Time Analyzer**

## **Question Code: Q9301**

**Difficulty Level:** Medium
**Technology:** NumPy
**Total Marks:** 20
**Assessment SOP:** Independent test setup, latest-only report, no final score print

## **Assessment Instructions**

Open the Learnlytica assessment tool.

Enter your **Email address**, enter the **Question ID**, and click **Start Assessment**.

Open VSCode and implement your solution only in:

```python
solution.py
```

After completing the implementation:

1. Click **Run Tests**.
2. Review the test results.
3. Click **Validate**.
4. Once satisfied with your attempt, click **Submit**.
5. Click **End Assessment**.

> **Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.**

---

# **📌 Problem Statement**

A video streaming platform tracks daily watch-time minutes for a trending show.

Each value in the NumPy array represents the total watch minutes recorded for one day.

Your task is to build function-based NumPy utilities to:

* Create a watch-time array
* Validate watch-time data
* Calculate watch-time metrics
* Categorize watch levels
* Find the longest watch growth streak
* Format watch-time values

---

# **📌 Function Rules**

* Do not create a class.
* Implement all functions at module level.
* Import NumPy as `np`.
* Do not use Pandas.
* Return NumPy arrays where array output is expected.

---

# **✅ 1. Create Watch Array**

Creates a NumPy array from the given watch-time data.

## **Function Prototype**

```python
def create_watch_array(watch_data: list) -> np.ndarray:
```

## **Example Input**

```python
create_watch_array([750, 1250, 2750, 3400])
```

## **Expected Output**

```python
np.array([750, 1250, 2750, 3400], dtype=np.int64)
```

## **Implementation Flow**

* Convert the input list into a NumPy array.
* Use `dtype=np.int64`.
* Return the resulting NumPy array.

---

# **✅ 2. Validate Watch Array**

Checks whether the watch-time array contains valid data.

## **Function Prototype**

```python
def validate_watch_array(watch_array: np.ndarray) -> bool:
```

## **Example Input**

```python
validate_watch_array(np.array([500, -10, 1200]))
```

## **Expected Output**

```python
False
```

## **Implementation Flow**

* If the array is empty, return `False`.
* Use `np.issubdtype(watch_array.dtype, np.number)` to confirm that the array contains numeric data.
* Return `False` if any value is negative.
* Return `True` only if all validations pass.

## **Hidden Test Focus**

* Empty arrays must return `False`.
* Non-numeric arrays must return `False`.

---

# **✅ 3. Compute Watch Metrics**

Calculates total, average, and maximum watch-time minutes.

## **Function Prototype**

```python
def compute_watch_metrics(watch_array: np.ndarray) -> tuple:
```

## **Example Input**

```python
compute_watch_metrics(np.array([600, 900, 1500]))
```

## **Expected Output**

```python
(3000, 1000.0, 1500)
```

## **Implementation Flow**

* Use `np.sum()` to calculate total minutes.
* Use `np.mean()` to calculate average minutes.
* Use `np.max()` to calculate maximum minutes.
* Convert total minutes to `int`.
* Convert maximum minutes to `int`.
* Round average minutes to 2 decimal places.
* Return:

```python
(total_minutes, average_minutes, maximum_minutes)
```

---

# **✅ 4. Categorize Watch Levels**

Classifies each watch-time value into Low, Medium, or High Watch.

## **Function Prototype**

```python
def categorize_watch_levels(watch_array: np.ndarray) -> np.ndarray:
```

## **Example Input**

```python
categorize_watch_levels(np.array([800, 1500, 3200]))
```

## **Expected Output**

```python
np.array(["Low Watch", "Medium Watch", "High Watch"])
```

## **Implementation Flow**

Use `np.where()` for vectorized labeling.

Apply the following rules:

```text
Minutes < 1000        -> Low Watch
1000 to 2999          -> Medium Watch
Minutes >= 3000       -> High Watch
```

Return the resulting label array.

## **Hidden Test Focus**

The following boundary conditions must be handled correctly:

```text
999  -> Low Watch
1000 -> Medium Watch
2999 -> Medium Watch
3000 -> High Watch
```

---

# **✅ 5. Longest Watch Growth Streak**

Returns the length of the longest consecutive increasing watch-time streak.

## **Function Prototype**

```python
def longest_watch_growth_streak(watch_array: np.ndarray) -> int:
```

## **Example Input**

```python
longest_watch_growth_streak(
    np.array([400, 700, 1000, 800, 1200])
)
```

## **Expected Output**

```python
3
```

## **Implementation Flow**

* If the array is empty, return `0`.
* If the array contains only one value, return `1`.
* Initialize:

```python
max_streak = 1
current_streak = 1
```

* Loop from index `1` to the end of the array.
* If the current value is greater than the previous value, increase `current_streak`.
* Update `max_streak` whenever the current streak becomes larger.
* If growth breaks, reset `current_streak` to `1`.
* Return `max_streak`.

---

# **✅ 6. Format Watch Minutes**

Formats each watch-time value using comma separators.

## **Function Prototype**

```python
def format_watch_minutes(watch_array: np.ndarray) -> np.ndarray:
```

## **Example Input**

```python
format_watch_minutes(np.array([950, 12500, 800000]))
```

## **Expected Output**

```python
np.array(["950", "12,500", "800,000"])
```

## **Implementation Flow**

* Declare an empty list.
* Use a `for` loop to process each value.
* Format each value using:

```python
f"{value:,}"
```

* Add each formatted value to the list.
* Convert the formatted list into a NumPy array.
* Return the resulting array.

---

# **📌 Driver and SOP Notes**
