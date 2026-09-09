Water Quality Monitoring System records

**Question Code:**: Q4444
Open the Learnlytica assessment tool
 Enter your Email address, and then enter the Question ID and click on start assessment.
 Once started, click on VSCode, and it will directly open the solution.py file of the question, and write your code there.
 Once you have written the code, come back to the tool and click on run tests. After executing the run tests, click on Validate.
 After completing that validation, and you are satisfied with your attempt, you can click on submit in the tool and then click End assessment.

📌

## Problem Statement

A Water Quality Monitoring System records pollution readings collected from different testing points. Each reading represents the pollution level in ppm.
Your task is to implement a NumPy-based analyzer that can:
create a NumPy array from raw readings
validate whether readings are usable
compute basic statistics
reduce extreme readings
label high pollution values
format readings for final reporting

📌

## Class Creation

class WaterQualityAnalyzer:
No need to use init method.
If needed, follow recommendation:
def __init__(self):
 pass

📌

## Operations

✅

1. Create Quality Array
📌 Converts raw pollution readings into a NumPy array.
🔹

Function Prototype:
def create_quality_array(self, readings: list) -> np.ndarray:
🔹

Example Input:
create_quality_array([12.5, 45.0, 105.0, 80.5])
🔹

Expected Output:
array([ 12.5,

45. ,

105. , 80.5])
🔹

## Implementation Flow

:
💡 Import NumPy as np.
💡 Use np.array() to convert the input list into a NumPy array.
💡 Do not change the order of readings.
💡 Do not filter or modify readings in this function.
💡 Return the created NumPy array.

✅

2. Validate Quality Array
📌 Checks whether all readings are valid non-negative values.
🔹

Function Prototype:
def validate_quality_array(self, arr: np.ndarray) -> bool:
🔹

Example Input:
validate_quality_array(np.array([10, 20, 30]))
🔹

Expected Output:
True
🔹

Example Input:
validate_quality_array(np.array([15, -5, 30]))
🔹

Expected Output:
False
🔹

## Implementation Flow

:
💡 First check whether the array is empty.
💡 If array size is 0, return False.
💡 Use np.all() to check whether all values are greater than or equal to

0.
💡 Return True if all values are valid.
💡 Return False if any value is negative.
💡 Hidden test focus: empty array should return False.

✅

3. Compute Quality Statistics
📌 Returns total, average, and maximum pollution reading.
🔹

Function Prototype:
def compute_quality_statistics(self, arr: np.ndarray) -> tuple:
🔹

Example Input:
compute_quality_statistics(np.array([10.0, 25.0, 40.0]))
🔹

Expected Output:
(75.0, 25.0, 40.0)
🔹

## Implementation Flow

:
💡 Use np.sum() to calculate total pollution reading.
💡 Use np.mean() to calculate average pollution reading.
💡 Use np.max() to calculate maximum pollution reading.
💡 Store the three results in variables such as total, average, and maximum.
💡 Return the values as a tuple in this order:
(total, average, maximum)
💡 Do not return a list or dictionary.

✅

4. Filter Extreme Levels
📌 Reduces readings greater than or equal to 100 by 10%.
🔹

Function Prototype:
def filter_extreme_levels(self, arr: np.ndarray) -> np.ndarray:
🔹

Example Input:
filter_extreme_levels(np.array([80, 100, 120]))
🔹

Expected Output:
array([ 80., 90., 108.])
🔹

## Implementation Flow

:
💡 Use np.where() to check readings greater than or equal to

100.
💡 If a reading is greater than or equal to 100, multiply it by 0.9.
💡 If a reading is below 100, keep it unchanged.
💡 Return the updated NumPy array.
💡 Hidden test focus: value exactly 100 should also be reduced to

90.

✅

5. Label High Pollution
📌 Labels readings as "High" if pollution reading is greater than 75, otherwise "Normal".
🔹

Function Prototype:
def label_high_pollution(self, arr: np.ndarray) -> np.ndarray:
🔹

Example Input:
label_high_pollution(np.array([30, 90, 60]))
🔹

Expected Output:
array(['Normal', 'High', 'Normal'], dtype='<U6')
🔹

## Implementation Flow

:
💡 Use np.where() to check each reading.
💡 If reading is greater than 75, assign label "High".
💡 Otherwise assign label "Normal".
💡 Return the label array.
💡 Do not return a Python list.
💡 Do not modify the original numeric readings.

✅

6. Format Quality Readings
📌 Formats pollution readings as strings with two decimal places followed by " ppm".
🔹

Function Prototype:
def format_quality_readings(self, arr: np.ndarray) -> np.ndarray:
🔹

Example Input:
format_quality_readings(np.array([22.0, 35.756]))
🔹

Expected Output:
array(['22.00 ppm', '35.76 ppm'], dtype='<U9')
🔹

## Implementation Flow

:
💡 Iterate through the NumPy array.
💡 Format each reading using two decimal places.
💡 Add " ppm" after each formatted value.
💡 Store all formatted values in a list.
💡 Convert the list into a NumPy array using np.array().
💡 Return the NumPy array.
Example formatting logic:
f"{value:.2f} ppm"
💡 Hidden test focus: decimal values should be rounded to exactly two decimal places.
