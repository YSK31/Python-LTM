import pandas as pd
import numpy as np
import re
import os

class AttendanceAnalyzer:
  def __init__(self):
    pass
  
  def create_attendance_df(self, data):
    df = pd.DataFrame(data, columns = ["EmployeeID", "Department", "Date", "Attendance"])
    return df
  
  def compute_monthly_attendance_rate(self, df):
    df["Month"] = df["Date"].str[:7]
    total = df.groupby(["EmployeeID", "Month"]).size().reset_index(name = "Total")
    present_df = df[df['Attendance'] == "Present"]
    present = present_df.groupby(["EmployeeID", "Month"]).size().reset_index(name = "Present")
    result = total.merge(
        present,
        on = ["EmployeeID", "Month"],
        how = "left"
    )
    result["Present"] = result["Present"].fillna(0)

    result["Attendance Rate"] = (result["Present"] / result["Total"]) * 100
    return result[["EmployeeID", "Month", "Attendance Rate"]]
  
  def add_absence_flag(self, df):
    df["IsAbsent"] = (df["Attendance"] == "Absent").astype(int)
    return df

  def high_absentees(self, df, threshold):
    absent_df = df[df["Attendance"] == "Absent"]
    count_df = absent_df.groupby("EmployeeID").size().reset_index(name = "Absent Count")
    return count_df[count_df["Absent Count"] > threshold]
  
  def department_attendance_summary(self, df):
    result = pd.crosstab(df["Department"], df["Attendance"])
    result.columns.name = None
    result = result.reindex(columns = ["Present", "Absent", "Leave"], fill_value = 0)
    return result
