import pandas as pd

class ShiftAttendanceAnalyzer:
    def create_attendance_df(self, data):
        return pd.DataFrame(data, columns=["EmployeeID", "Department", "ShiftDate", "Status", "OvertimeHours"])

    def standardize_shift_date(self, df):
        result = df.copy()
        result["ShiftDate"] = pd.to_datetime(result["ShiftDate"], errors="coerce")
        return result

    def add_attendance_points(self, df):
        result = df.copy()
        result["AttendancePoints"] = result["Status"].map({"Present": 2, "Leave": 1, "Absent": 0})
        return result

    def department_attendance_summary(self, df):
        result = df.groupby("Department").agg(
            TotalRecords=("Department", "size"),
            PresentCount=("Status", lambda x: (x == "Present").sum()),
            TotalOvertimeHours=("OvertimeHours", "sum")
        ).reset_index()
        return result.sort_values("Department").reset_index(drop=True)

    def filter_overtime_records(self, df, hours):
        return df[df["OvertimeHours"] >= hours].sort_values(
            ["OvertimeHours", "EmployeeID"], ascending=[False, True]
        ).reset_index(drop=True)

    def department_status_table(self, df):
        result = pd.crosstab(df["Department"], df["Status"]).reindex(
            columns=["Present", "Absent", "Leave"], fill_value=0
        ).reset_index()
        return result.sort_values("Department").reset_index(drop=True)

if __name__ == "__main__":
    data = [
        ["E101", "IT", "2026-08-01", "Present", 2.5],
        ["E102", "HR", "2026-08-01", "Leave", 0],
        ["E103", "IT", "2026-08-02", "Absent", 1.0],
        ["E104", "Sales", "2026-08-02", "Present", 3.0],
        ["E105", "IT", "2026-08-03", "Present", 4.0],
    ]
    a = ShiftAttendanceAnalyzer()
    df = a.create_attendance_df(data)
    dated = a.standardize_shift_date(df)

    print("1. create_attendance_df")
    print(df)
    print("\n2. standardize_shift_date")
    print(dated)
    print("\n3. add_attendance_points")
    print(a.add_attendance_points(df))
    print("\n4. department_attendance_summary")
    print(a.department_attendance_summary(df))
    print("\n5. filter_overtime_records")
    print(a.filter_overtime_records(df, 2.5))
    print("\n6. department_status_table")
    print(a.department_status_table(df))
