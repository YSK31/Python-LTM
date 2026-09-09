# **Sensor Reading Analysis System**

## **Question Code: Q391**

## **Milestone 2**

## **Assessment Instructions**

Open the Learnlytica assessment tool.

Enter your **Email address**, enter the **Question ID**, and click **Start Assessment**.

Once the assessment starts, click on **VSCode**. It will directly open the `solution.py` file. Write your code only in this file.

Once you have written the code, come back to the tool and click **Run Tests**.

After executing the tests, click **Validate**.

After completing the validation and once you are satisfied with your attempt, click **Submit** and then click **End Assessment**.

---

# **📌 Class Creation**

```python
class SensorAnalyzer:
```

---

# **✅ 1. Create Sensor Array**

Creates a NumPy array from the given sensor readings.

## **Function Prototype**

```python
def create_sensor_array(self, sensor_values: list) -> np.ndarray:
```

## **Example Input**

```python
create_sensor_array([28.5, 415.0, 30.7, 92.1])
```

## **Expected Output**

```python
np.array([28.5, 415.0, 30.7, 92.1])
```

## **Implementation Flow**

* Convert the input list into a NumPy array.
* Ensure all elements are stored using a float data type.
* Return the resulting NumPy array.

---

# **✅ 2. Validate Sensor Array**

Checks whether the sensor array contains valid readings.

## **Function Prototype**

```python
def validate_sensor_array(self, sensor_array: np.ndarray) -> bool:
```

## **Example Input**

```python
validate_sensor_array(np.array([923, -40, 810]))
```

## **Expected Output**

```python
False
```

## **Implementation Flow**

* Check whether the array is non-empty.
* Ensure all values are positive.
* Return `True` if all validations pass.
* Otherwise, return `False`.

---

# **✅ 3. Compute Sensor Statistics**

Calculates total, average, and maximum values from the sensor readings.

## **Function Prototype**

```python
def compute_sensor_statistics(self, sensor_array: np.ndarray) -> tuple:
```

## **Example Input**

```python
compute_sensor_statistics(np.array([20.0, 60.0, 40.0]))
```

## **Expected Output**

```python
(120.0, 40.0, 60.0)
```

## **Implementation Flow**

* Calculate the total of all sensor readings.
* Calculate the average of all sensor readings.
* Calculate the maximum sensor reading.
* Round the average to `1` decimal place.
* Return the result as:

```python
(total, average, maximum)
```

---

# **✅ 4. Filter Extreme Readings**

Reduces sensor readings that are greater than or equal to the specified threshold.

## **Function Prototype**

```python
def filter_extreme_readings(self, sensor_array: np.ndarray) -> np.ndarray:
```

## **Example Input**

```python
filter_extreme_readings(np.array([100.0, 50.0, 60.0]))
```

## **Expected Output**

```python
np.array([90.0, 45.0, 54.0])
```

## **Implementation Flow**

* Convert all elements to float using the `astype()` method.
* Apply a `10%` reduction to readings greater than or equal to `50.0`.
* Leave readings below `50.0` unchanged.
* Return the updated NumPy array.

---

# **✅ 5. Label High Sensors**

Labels each sensor reading as either `"High"` or `"Normal"` based on the mean value.

## **Function Prototype**

```python
def label_high_sensors(self, sensor_array: np.ndarray) -> np.ndarray:
```

## **Example Input**

```python
label_high_sensors(np.array([100.0, 50.0, 60.0]))
```

## **Expected Output**

```python
np.array(["High", "Normal", "Normal"])
```

## **Implementation Flow**

* Calculate the mean of the given sensor array.
* Compare every sensor reading with the mean.
* If a reading is greater than the mean, label it as `"High"`.
* Otherwise, label it as `"Normal"`.
* Return the resulting NumPy array.

---

# **✅ 6. Format Sensor Readings**

Formats each sensor reading as a string with two decimal places followed by `"units"`.

## **Function Prototype**

```python
def format_sensor_readings(self, sensor_array: np.ndarray) -> np.ndarray:
```

## **Example Input**

```python
format_sensor_readings(np.array([55.0, 66.0]))
```

## **Expected Output**

```python
np.array(["55.00 units", "66.00 units"])
```

## **Implementation Flow**

* Convert each sensor reading into a formatted string.
* Use the following format:

```python
f"{x:.2f} units"
```

* Store all formatted values in a NumPy array.
* Return the formatted array.
