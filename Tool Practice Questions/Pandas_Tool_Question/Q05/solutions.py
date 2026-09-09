import pandas as pd

class SalesListManager:
    def create_dataframe(self, data, columns):
        df = pd.DataFrame(data, columns=columns)
        df["OrderID"] = pd.to_numeric(df["OrderID"], errors="coerce").astype("Int64")
        df["Units"] = pd.to_numeric(df["Units"], errors="coerce").astype("Int64")
        df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
        df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
        df["CustomerName"] = df["CustomerName"].astype(str).str.strip().str.title()
        df["Category"] = df["Category"].astype(str).str.strip()
        df["Region"] = df["Region"].astype(str).str.strip()
        df["Channel"] = df["Channel"].astype(str).str.strip()
        df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce", format="mixed")
        return df

    def get_customer_names(self, df):
        return df["CustomerName"].tolist()

    def groupby_region_category_units(self, df):
        return df.groupby(["Region", "Category"], as_index=False)["Units"].sum()

    def compute_revenue(self, df):
        result = df.copy()
        result["Revenue"] = (
            result["Units"].fillna(0)
            * result["UnitPrice"].fillna(0)
            * (1 - result["Discount"].fillna(0))
        )
        return result

    def assign_amount_flag(self, df):
        result = self.compute_revenue(df) if "Revenue" not in df.columns else df.copy()
        result["AmountFlag"] = "Low"
        result.loc[result["Revenue"] >= 300, "AmountFlag"] = "Medium"
        result.loc[result["Revenue"] >= 800, "AmountFlag"] = "High"
        return result

    def build_category_region_crosstab(self, df):
        return pd.crosstab(df["Category"], df["Region"])

    def filter_by_region_min_units(self, df, region, min_units):
        return df[(df["Region"] == region) & (df["Units"] >= min_units)].reset_index(drop=True)

    def compute_region_unit_share(self, df):
        category_units = df.groupby(["Region", "Category"], as_index=False)["Units"].sum()
        region_units = df.groupby("Region", as_index=False)["Units"].sum().rename(columns={"Units": "RegionUnits"})
        result = pd.merge(category_units, region_units, on="Region")
        result["UnitShare"] = result["Units"] / result["RegionUnits"]
        return result[["Region", "Category", "Units", "RegionUnits", "UnitShare"]]

    def total_units(self, df):
        return int(df["Units"].sum())

    def average_unit_price(self, df):
        return float(df["UnitPrice"].mean())

    def top_n_orders_by_revenue(self, df, n):
        result = self.compute_revenue(df) if "Revenue" not in df.columns else df.copy()
        return result.nlargest(n, "Revenue").reset_index(drop=True)

    def bottom_n_orders_by_revenue(self, df, n):
        result = self.compute_revenue(df) if "Revenue" not in df.columns else df.copy()
        return result.nsmallest(n, "Revenue").reset_index(drop=True)

    def channel_counts(self, df):
        return df["Channel"].value_counts()

    def fill_missing_unitprice_with_mean(self, df):
        result = df.copy()
        result["UnitPrice"] = result["UnitPrice"].fillna(result["UnitPrice"].mean())
        return result

    def drop_rows_missing_discount(self, df):
        return df.dropna(subset=["Discount"]).reset_index(drop=True)

    def orders_with_missing_values(self, df):
        return df[df.isna().any(axis=1)].reset_index(drop=True)

    def filter_by_channel_and_flag(self, df, channel, flag):
        result = self.assign_amount_flag(df) if "AmountFlag" not in df.columns else df.copy()
        return result[(result["Channel"] == channel) & (result["AmountFlag"] == flag)].reset_index(drop=True)

    def summary_stats(self, df):
        result = self.compute_revenue(df) if "Revenue" not in df.columns else df.copy()
        return result[["Units", "UnitPrice", "Revenue"]].agg(["sum", "mean", "min", "max"])

    def monthly_revenue(self, df):
        result = self.compute_revenue(df) if "Revenue" not in df.columns else df.copy()
        result["OrderDate"] = pd.to_datetime(result["OrderDate"], errors="coerce", format="mixed")
        series = result.groupby(result["OrderDate"].dt.to_period("M"))["Revenue"].sum()
        series.index = series.index.astype(str)
        return series

    def add_discount_amount_column(self, df):
        result = df.copy()
        result["DiscountAmount"] = (
            result["Units"].fillna(0)
            * result["UnitPrice"].fillna(0)
            * result["Discount"].fillna(0)
        )
        return result

if __name__ == "__main__":
    columns = ["OrderID", "CustomerName", "Category", "Region", "Units", "UnitPrice", "Discount", "Channel", "OrderDate"]
    data = [
        [101, "  rahul ", "Laptop", "South", 5, 500.0, 0.10, " Online ", "2026-01-10"],
        [102, "priya", "Phone", "South", 3, 300.0, None, "Store", "2026/01/15"],
        [103, " arun", "Laptop", "North", 8, None, 0.05, "Online", "2026-02-05"],
        [104, "meena", "Tablet", "North", 2, 450.0, 0.20, "Store", "2026-02-20"],
    ]
    a = SalesListManager()
    df = a.create_dataframe(data, columns)

    print("1. create_dataframe")
    print(df)
    print("\n2. get_customer_names")
    print(a.get_customer_names(df))
    print("\n3. groupby_region_category_units")
    print(a.groupby_region_category_units(df))
    print("\n4. compute_revenue")
    print(a.compute_revenue(df))
    revenue_df = a.compute_revenue(df)
    print("\n5. assign_amount_flag")
    print(a.assign_amount_flag(revenue_df))
    print("\n6. build_category_region_crosstab")
    print(a.build_category_region_crosstab(df))
    print("\n7. filter_by_region_min_units")
    print(a.filter_by_region_min_units(df, "South", 3))
    print("\n8. compute_region_unit_share")
    print(a.compute_region_unit_share(df))
    print("\n9. total_units")
    print(a.total_units(df))
    print("\n10. average_unit_price")
    print(a.average_unit_price(df))
    print("\n11. top_n_orders_by_revenue")
    print(a.top_n_orders_by_revenue(df, 2))
    print("\n12. bottom_n_orders_by_revenue")
    print(a.bottom_n_orders_by_revenue(df, 2))
    print("\n13. channel_counts")
    print(a.channel_counts(df))
    print("\n14. fill_missing_unitprice_with_mean")
    print(a.fill_missing_unitprice_with_mean(df))
    print("\n15. drop_rows_missing_discount")
    print(a.drop_rows_missing_discount(df))
    print("\n16. orders_with_missing_values")
    print(a.orders_with_missing_values(df))
    print("\n17. filter_by_channel_and_flag")
    print(a.filter_by_channel_and_flag(df, "Online", "High"))
    print("\n18. summary_stats")
    print(a.summary_stats(df))
    print("\n19. monthly_revenue")
    print(a.monthly_revenue(df))
    print("\n20. add_discount_amount_column")
    print(a.add_discount_amount_column(df))
