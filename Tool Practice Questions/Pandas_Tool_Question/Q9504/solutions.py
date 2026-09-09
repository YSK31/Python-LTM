import pandas as pd

class SubscriptionRevenueAnalyzer:
    def create_subscription_df(self, data):
        return pd.DataFrame(data, columns=["SubscriberID", "Plan", "StartDate", "MonthlyFee", "Status"])

    def clean_subscription_data(self, df):
        result = df.copy()
        result = result.dropna(subset=["SubscriberID"])
        result["Plan"] = result["Plan"].fillna("Unknown")
        result["MonthlyFee"] = result["MonthlyFee"].fillna(0)
        return result.reset_index(drop=True)

    def add_active_revenue(self, df):
        result = df.copy()
        result["ActiveRevenue"] = result["MonthlyFee"].where(result["Status"] == "Active", 0)
        return result

    def plan_revenue_summary(self, df):
        result = df.groupby("Plan").agg(
            Subscribers=("Plan", "size"),
            ActiveSubscribers=("Status", lambda x: (x == "Active").sum()),
            TotalActiveRevenue=("ActiveRevenue", "sum")
        ).reset_index()
        return result.sort_values("Plan").reset_index(drop=True)

    def subscriptions_from_date(self, df, start_date):
        result = df.copy()
        result["StartDate"] = pd.to_datetime(result["StartDate"], errors="coerce")
        cutoff = pd.to_datetime(start_date)
        return result[result["StartDate"] >= cutoff].sort_values(
            ["StartDate", "SubscriberID"]
        ).reset_index(drop=True)

    def top_plans_by_revenue(self, df, n):
        result = df.groupby("Plan")["ActiveRevenue"].sum().reset_index(name="TotalActiveRevenue")
        result = result.sort_values(["TotalActiveRevenue", "Plan"], ascending=[False, True])
        return result.head(n).reset_index(drop=True)

if __name__ == "__main__":
    data = [
        ["S101", "Basic", "2026-08-01", 299, "Active"],
        ["S102", "Pro", "2026/08/03", 599, "Active"],
        ["S103", None, "2026-08-05", None, "Cancelled"],
        [None, "Basic", "2026-08-06", 299, "Active"],
        ["S104", "Pro", "2026-08-10", 599, "Paused"],
    ]
    a = SubscriptionRevenueAnalyzer()
    df = a.create_subscription_df(data)
    clean = a.clean_subscription_data(df)
    revenue = a.add_active_revenue(clean)

    print("1. create_subscription_df")
    print(df)
    print("\n2. clean_subscription_data")
    print(clean)
    print("\n3. add_active_revenue")
    print(revenue)
    print("\n4. plan_revenue_summary")
    print(a.plan_revenue_summary(revenue))
    print("\n5. subscriptions_from_date")
    print(a.subscriptions_from_date(revenue, "2026-08-04"))
    print("\n6. top_plans_by_revenue")
    print(a.top_plans_by_revenue(revenue, 2))
