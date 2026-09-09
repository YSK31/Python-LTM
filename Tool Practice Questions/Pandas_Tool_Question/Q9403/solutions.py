import pandas as pd

class GreenhouseAnalyzer:
    def create_production_df(self, data):
        return pd.DataFrame(data, columns=["PlotID", "Date", "YieldKg", "Temperature", "DowntimeMinutes"])

    def total_yield_per_plot(self, df):
        return df.groupby("PlotID")["YieldKg"].sum().reset_index().rename(columns={"YieldKg": "TotalYield"})

    def add_yield_per_active_min(self, df):
        result = df.copy()
        active_minutes = 1440 - result["DowntimeMinutes"]
        result["YieldPerMin"] = (result["YieldKg"] / active_minutes).round(2)
        return result

    def categorize_temperature_band(self, df):
        result = df.copy()
        result["TempBand"] = "Cool"
        result.loc[result["Temperature"] >= 20, "TempBand"] = "Warm"
        result.loc[result["Temperature"] >= 30, "TempBand"] = "Hot"
        return result

    def frequent_downtime_rows(self, df, n):
        return df[df["DowntimeMinutes"] > n]

    def clean_and_top_yield_days(self, df):
        return df.dropna().sort_values("YieldKg", ascending=False).reset_index(drop=True)

if __name__ == "__main__":
    data = [
        ["P1", "2026-08-01", 120.0, 19.5, 10],
        ["P2", "2026-08-01", 90.0, 24.0, 25],
        ["P1", "2026-08-02", 150.0, 30.0, 5],
        ["P3", "2026-08-02", 80.0, 31.5, 40],
    ]
    a = GreenhouseAnalyzer()
    df = a.create_production_df(data)

    print("1. create_production_df")
    print(df)
    print("\n2. total_yield_per_plot")
    print(a.total_yield_per_plot(df))
    print("\n3. add_yield_per_active_min")
    print(a.add_yield_per_active_min(df))
    print("\n4. categorize_temperature_band")
    print(a.categorize_temperature_band(df))
    print("\n5. frequent_downtime_rows")
    print(a.frequent_downtime_rows(df, 20))
    print("\n6. clean_and_top_yield_days")
    dirty = pd.concat([df, pd.DataFrame([["P4", None, None, 22.0, 5]], columns=df.columns)], ignore_index=True)
    print(a.clean_and_top_yield_days(dirty))
