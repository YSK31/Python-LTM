import pandas as pd

class CampaignDashboard:
    def create_campaign_df(self, campaign_data):
        return pd.DataFrame(campaign_data, columns=["Campaign", "Channel", "Outcome", "Leads"])

    def campaign_lead_summary(self, df):
        result = df.groupby("Campaign")["Leads"].agg(["sum", "mean"]).reset_index()
        result.columns = ["Campaign", "Total Leads", "Average Leads"]
        return result

    def add_outcome_points(self, df):
        result = df.copy()
        result["Points"] = result["Outcome"].map({"Converted": 5, "Interested": 2, "Ignored": 0})
        return result

    def filter_high_leads(self, df, n):
        return df[df["Leads"] > n]

    def compute_conversion_rate(self, df):
        total = df.groupby("Campaign").size().reset_index(name="Total")
        converted = df[df["Outcome"] == "Converted"].groupby("Campaign").size().reset_index(name="Converted")
        result = pd.merge(total, converted, on="Campaign", how="left")
        result["Converted"] = result["Converted"].fillna(0)
        result["Conversion Rate"] = (result["Converted"] / result["Total"] * 100).round(1)
        return result[["Campaign", "Conversion Rate"]]

    def top_campaigns_by_points(self, df, n):
        result = df.groupby("Campaign")["Points"].sum().reset_index()
        result = result.rename(columns={"Points": "Total Points"})
        return result.sort_values("Total Points", ascending=False).head(n).reset_index(drop=True)

if __name__ == "__main__":
    data = [
        ["Festive", "Email", "Converted", 45],
        ["Festive", "SMS", "Interested", 30],
        ["Winter", "SMS", "Ignored", 20],
        ["Winter", "Email", "Converted", 35],
        ["Summer", "Email", "Interested", 25],
    ]
    a = CampaignDashboard()
    df = a.create_campaign_df(data)
    scored = a.add_outcome_points(df)

    print("1. create_campaign_df")
    print(df)
    print("\n2. campaign_lead_summary")
    print(a.campaign_lead_summary(df))
    print("\n3. add_outcome_points")
    print(scored)
    print("\n4. filter_high_leads")
    print(a.filter_high_leads(df, 30))
    print("\n5. compute_conversion_rate")
    print(a.compute_conversion_rate(df))
    print("\n6. top_campaigns_by_points")
    print(a.top_campaigns_by_points(scored, 2))
