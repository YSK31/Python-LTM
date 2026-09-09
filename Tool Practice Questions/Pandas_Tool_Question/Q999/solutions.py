import pandas as pd

class HospitalAppointmentAnalyzer:
    def create_appointment_df(self, appointment_data):
        return pd.DataFrame(appointment_data, columns=["AppointmentID", "DoctorID", "PatientName", "ConsultationFee"])

    def create_doctor_df(self, doctor_data):
        return pd.DataFrame(doctor_data, columns=["DoctorID", "DoctorName", "Specialization", "Location"])

    def merge_doctor_info(self, appointment_df, doctor_df):
        return pd.merge(appointment_df, doctor_df, on="DoctorID", how="inner")

    def get_repeat_doctors(self, appointment_df):
        result = appointment_df.groupby("DoctorID").size().reset_index(name="AppointmentCount")
        return result[result["AppointmentCount"] > 1].reset_index(drop=True)

    def calculate_total_revenue(self, appointment_df):
        result = appointment_df.groupby("DoctorID")["ConsultationFee"].sum().reset_index()
        return result.rename(columns={"ConsultationFee": "TotalRevenue"})

    def location_wise_patients(self, merged_df):
        result = merged_df.groupby("Location")["PatientName"].nunique().reset_index()
        return result.rename(columns={"PatientName": "UniquePatients"})

if __name__ == "__main__":
    appointments = [
        [501, "D101", "Ravi", 800.0],
        [502, "D102", "Neha", 1200.0],
        [503, "D101", "Amit", 1000.0],
        [504, "D101", "Ravi", 900.0],
    ]
    doctors = [
        ["D101", "Dr. Sharma", "Cardiology", "Mumbai"],
        ["D102", "Dr. Mehta", "Dermatology", "Delhi"],
    ]
    a = HospitalAppointmentAnalyzer()
    appointments_df = a.create_appointment_df(appointments)
    doctors_df = a.create_doctor_df(doctors)
    merged = a.merge_doctor_info(appointments_df, doctors_df)

    print("1. create_appointment_df")
    print(appointments_df)
    print("\n2. create_doctor_df")
    print(doctors_df)
    print("\n3. merge_doctor_info")
    print(merged)
    print("\n4. get_repeat_doctors")
    print(a.get_repeat_doctors(appointments_df))
    print("\n5. calculate_total_revenue")
    print(a.calculate_total_revenue(appointments_df))
    print("\n6. location_wise_patients")
    print(a.location_wise_patients(merged))
