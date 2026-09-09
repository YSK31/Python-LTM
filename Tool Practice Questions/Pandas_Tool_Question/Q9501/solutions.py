import pandas as pd

class LibraryBorrowingAnalyzer:
    def create_borrowing_df(self, data):
        return pd.DataFrame(data, columns=["MemberID", "Category", "BorrowDate", "ReturnDate", "LateFee"])

    def clean_late_fees(self, df):
        result = df.copy()
        result["LateFee"] = result["LateFee"].fillna(0).clip(lower=0)
        return result

    def add_borrowing_days(self, df):
        result = df.copy()
        result["BorrowDate"] = pd.to_datetime(result["BorrowDate"], errors="coerce")
        result["ReturnDate"] = pd.to_datetime(result["ReturnDate"], errors="coerce")
        result["BorrowingDays"] = (result["ReturnDate"] - result["BorrowDate"]).dt.days
        return result

    def member_borrowing_summary(self, df):
        result = df.groupby("MemberID").agg(
            BooksBorrowed=("MemberID", "size"),
            TotalLateFee=("LateFee", "sum")
        ).reset_index()
        return result.sort_values("MemberID").reset_index(drop=True)

    def filter_long_borrowings(self, df, days):
        return df[df["BorrowingDays"] > days]

    def top_members_by_fee(self, df, n):
        result = df.groupby("MemberID")["LateFee"].sum().reset_index(name="TotalLateFee")
        result = result.sort_values(["TotalLateFee", "MemberID"], ascending=[False, True])
        return result.head(n).reset_index(drop=True)

if __name__ == "__main__":
    data = [
        ["M101", "Fiction", "2026-08-01", "2026-08-06", 0],
        ["M102", "Science", "2026-08-02", "2026-08-20", 25],
        ["M101", "History", "2026-08-10", "2026-08-18", -5],
        ["M103", "Fiction", "2026-08-05", "2026-08-07", None],
    ]
    a = LibraryBorrowingAnalyzer()
    df = a.create_borrowing_df(data)
    clean = a.clean_late_fees(df)
    dated = a.add_borrowing_days(clean)

    print("1. create_borrowing_df")
    print(df)
    print("\n2. clean_late_fees")
    print(clean)
    print("\n3. add_borrowing_days")
    print(dated)
    print("\n4. member_borrowing_summary")
    print(a.member_borrowing_summary(clean))
    print("\n5. filter_long_borrowings")
    print(a.filter_long_borrowings(dated, 7))
    print("\n6. top_members_by_fee")
    print(a.top_members_by_fee(clean, 2))
