# **Hospital Appointment Analyzer**

## **Question Code: Q999**

## **Assessment Instructions**

Open the Learnlytica assessment tool.

Enter your **Email address**, enter the **Question ID**, and click **Start Assessment**.

Once the assessment starts, click on **VSCode**. It will directly open the `solution.py` file. Write your code only in this file.

Once you have written the code, come back to the tool and click **Run Tests**.

After executing the tests, click **Validate**.

After completing the validation and once you are satisfied with your attempt, click **Submit** and then click **End Assessment**.

---

# **📌 Problem Statement**

A hospital tracks patient appointment records and stores doctor profile information separately.

Your task is to analyze hospital appointment activity, such as **doctor-wise appointments, total revenue, repeat doctors, and location-wise patient reach** using **Pandas and join operations**.

You are provided with two datasets:

**Appointment Logs**

* AppointmentID
* DoctorID
* PatientName
* ConsultationFee

**Doctor Profiles**

* DoctorID
* DoctorName
* Specialization
* Location

---

# **📌 Class Creation**

```python
class HospitalAppointmentAnalyzer:
```

No need to use the `__init__` method.

If needed, follow the recommendation:

```python
def __init__(self):
    pass
```

---

# **✅ 1. Create Appointment DataFrame**

Creates a DataFrame from raw appointment records.

## **Function Prototype**

```python
def create_appointment_df(self, appointment_data: list) -> pd.DataFrame:
```

## **Example Input**

```python
create_appointment_df([
    [501, "D101", "Ravi", 800.0],
    [502, "D102", "Neha", 1200.0],
    [503, "D101", "Amit", 1000.0]
])
```

## **Expected Output**

```text
   AppointmentID DoctorID PatientName  ConsultationFee
0            501     D101        Ravi            800.0
1            502     D102        Neha           1200.0
2            503     D101        Amit           1000.0
```

## **Implementation Flow**

* Import Pandas as `pd`.
* Create a DataFrame using `pd.DataFrame()`.
* Use exact columns: `["AppointmentID", "DoctorID", "PatientName", "ConsultationFee"]`.
* Do not rename, sort, or modify the input values.
* Return the created DataFrame.

---

# **✅ 2. Create Doctor Profile DataFrame**

Creates a DataFrame from raw doctor profile records.

## **Function Prototype**

```python
def create_doctor_df(self, doctor_data: list) -> pd.DataFrame:
```

## **Example Input**

```python
create_doctor_df([
    ["D101", "Dr. Sharma", "Cardiology", "Mumbai"],
    ["D102", "Dr. Mehta", "Dermatology", "Delhi"]
])
```

## **Expected Output**

```text
  DoctorID  DoctorName Specialization Location
0     D101  Dr. Sharma     Cardiology   Mumbai
1     D102   Dr. Mehta    Dermatology    Delhi
```

## **Implementation Flow**

* Create a DataFrame using `pd.DataFrame()`.
* Use exact columns: `["DoctorID", "DoctorName", "Specialization", "Location"]`.
* Keep all profile values as provided.
* Do not remove duplicate doctors in this function.
* Return the created DataFrame.

---

# **✅ 3. Merge Doctor Profile into Appointment Data**

Returns a merged DataFrame containing appointment details along with doctor profile information.

## **Function Prototype**

```python
def merge_doctor_info(
    self,
    appointment_df: pd.DataFrame,
    doctor_df: pd.DataFrame
) -> pd.DataFrame:
```

## **Example Input**

```python
merge_doctor_info(appointment_df, doctor_df)
```

## **Expected Output**

```text
   AppointmentID DoctorID PatientName  ConsultationFee  DoctorName Specialization Location
0            501     D101        Ravi            800.0  Dr. Sharma     Cardiology   Mumbai
1            502     D102        Neha           1200.0   Dr. Mehta    Dermatology    Delhi
2            503     D101        Amit           1000.0  Dr. Sharma     Cardiology   Mumbai
```

## **Implementation Flow**

* Use `pd.merge()` to combine appointment data and doctor profile data.
* Merge using the common column `"DoctorID"`.
* Use `how="inner"`.
* The merged DataFrame should contain appointment columns first and doctor profile columns after them.
* Return the merged DataFrame.

**Hidden Test Focus:** Appointments with Doctor IDs that are not available in the doctor profile data should not appear in the final output because an **inner join** is required.

---

# **✅ 4. Get Repeat Doctors**

Returns a DataFrame containing doctors who have more than one appointment.

## **Function Prototype**

```python
def get_repeat_doctors(
    self,
    appointment_df: pd.DataFrame
) -> pd.DataFrame:
```

## **Example Input**

```python
get_repeat_doctors(appointment_df)
```

## **Expected Output**

```text
  DoctorID  AppointmentCount
0     D101                 2
```

## **Implementation Flow**

* Group the appointment DataFrame by `"DoctorID"`.
* Use `.size()` to count the number of appointment rows for each doctor.
* Use `.reset_index(name="AppointmentCount")` to convert the grouped result into a DataFrame.
* Filter only doctors where `"AppointmentCount"` is greater than `1`.
* Use `reset_index(drop=True)` after filtering.
* Return the final DataFrame.

**Hidden Test Focus:** If no doctor has more than one appointment, return an empty DataFrame with the columns `["DoctorID", "AppointmentCount"]`.

---

# **✅ 5. Calculate Total Revenue per Doctor**

Returns the total consultation fee collected by each doctor.

## **Function Prototype**

```python
def calculate_total_revenue(
    self,
    appointment_df: pd.DataFrame
) -> pd.DataFrame:
```

## **Example Input**

```python
calculate_total_revenue(appointment_df)
```

## **Expected Output**

```text
  DoctorID  TotalRevenue
0     D101        1800.0
1     D102        1200.0
```

## **Implementation Flow**

* Group appointment data by `"DoctorID"`.
* Select the `"ConsultationFee"` column.
* Use `.sum()` to calculate the total consultation fee for each doctor.
* Use `.reset_index()` to convert the result into a DataFrame.
* Rename the `"ConsultationFee"` column to `"TotalRevenue"`.
* Return the final DataFrame.
* Do not calculate average revenue. Only total revenue is expected.

---

# **✅ 6. Get Location-wise Unique Patients**

Returns a DataFrame containing the number of unique patients for each location.

## **Function Prototype**

```python
def location_wise_patients(
    self,
    merged_df: pd.DataFrame
) -> pd.DataFrame:
```

## **Example Input**

```python
location_wise_patients(merged_df)
```

## **Expected Output**

```text
  Location  UniquePatients
0    Delhi               1
1   Mumbai               2
```

## **Implementation Flow**

* Use the merged DataFrame, not the raw appointment DataFrame.
* Group by `"Location"`.
* Select `"PatientName"`.
* Use `.nunique()` to count unique patients in each location.
* Use `.reset_index()` to convert the grouped result into a DataFrame.
* Rename the `"PatientName"` column to `"UniquePatients"`.
* Return the final DataFrame.

**Hidden Test Focus:** If the same patient appears multiple times in the same location, count that patient only once.
