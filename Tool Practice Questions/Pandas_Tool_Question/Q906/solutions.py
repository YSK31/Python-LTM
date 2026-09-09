import pandas as pd

class ReturnsAnalyzer:
    def create_orders_df(self, order_data):
        return pd.DataFrame(order_data, columns=["OrderID", "SellerID", "Category", "OrderDate", "OrderAmount"])

    def create_returns_df(self, return_data):
        return pd.DataFrame(return_data, columns=["OrderID", "ReturnDate", "RefundAmount", "Reason"])

    def merge_orders_returns(self, orders_df, returns_df):
        return pd.merge(orders_df, returns_df, on="OrderID", how="left")

    def category_refund_rate(self, merged_df):
        df = merged_df.copy()
        df["IsReturned"] = df["RefundAmount"].notna().astype(int)
        result = df.groupby("Category").agg(
            Orders=("OrderID", "size"),
            ReturnedOrders=("IsReturned", "sum")
        ).reset_index()
        result["RefundRate"] = (result["ReturnedOrders"] / result["Orders"] * 100).round(1)
        return result.sort_values("Category").reset_index(drop=True)

    def high_return_sellers(self, merged_df, n):
        df = merged_df.copy()
        if "IsReturned" not in df.columns:
            df["IsReturned"] = df["RefundAmount"].notna().astype(int)
        result = df[df["IsReturned"] == 1].groupby("SellerID").size().reset_index(name="ReturnCount")
        return result[result["ReturnCount"] > n].reset_index(drop=True)

    def clean_returns_data(self, returns_df):
        result = returns_df.dropna(subset=["Reason"])
        result = result[result["RefundAmount"].notna() & (result["RefundAmount"] > 0)]
        return result.reset_index(drop=True)

if __name__ == "__main__":
    orders = [
        [1, "S1", "Electronics", "2026-08-01", 1200.0],
        [2, "S2", "Fashion", "2026-08-02", 800.0],
        [3, "S1", "Electronics", "2026-08-03", 500.0],
        [4, "S3", "Grocery", "2026-08-04", 300.0],
    ]
    returns = [
        [1, "2026-08-05", 1200.0, "Damaged"],
        [3, "2026-08-06", 500.0, "Wrong Item"],
        [4, "2026-08-07", None, "Missing Amount"],
        [5, "2026-08-08", -20.0, "Invalid"],
    ]
    a = ReturnsAnalyzer()
    orders_df = a.create_orders_df(orders)
    returns_df = a.create_returns_df(returns)
    merged = a.merge_orders_returns(orders_df, returns_df)
    merged["IsReturned"] = merged["RefundAmount"].notna().astype(int)

    print("1. create_orders_df")
    print(orders_df)
    print("\n2. create_returns_df")
    print(returns_df)
    print("\n3. merge_orders_returns")
    print(merged)
    print("\n4. category_refund_rate")
    print(a.category_refund_rate(merged))
    print("\n5. high_return_sellers")
    print(a.high_return_sellers(merged, 1))
    print("\n6. clean_returns_data")
    print(a.clean_returns_data(returns_df))
