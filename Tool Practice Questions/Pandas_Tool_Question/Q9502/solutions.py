import pandas as pd

class InventoryMovementAnalyzer:
    def create_product_df(self, data):
        return pd.DataFrame(data, columns=["ProductID", "ProductName", "Category", "UnitPrice"])

    def create_movement_df(self, data):
        return pd.DataFrame(data, columns=["MovementID", "ProductID", "MovementType", "Quantity", "MovementDate"])

    def merge_product_movements(self, products_df, movements_df):
        return pd.merge(
            movements_df,
            products_df[["ProductID", "ProductName", "Category", "UnitPrice"]],
            on="ProductID",
            how="left",
            sort=False
        )[["MovementID", "ProductID", "MovementType", "Quantity", "MovementDate", "ProductName", "Category", "UnitPrice"]]

    def add_movement_value(self, df):
        result = df.copy()
        result["MovementValue"] = result["Quantity"] * result["UnitPrice"]
        return result

    def category_movement_summary(self, df):
        result = df.pivot_table(
            index="Category",
            columns="MovementType",
            values="Quantity",
            aggfunc="sum",
            fill_value=0
        ).reset_index()
        result["IN"] = result["IN"] if "IN" in result.columns else 0
        result["OUT"] = result["OUT"] if "OUT" in result.columns else 0
        result = result.rename(columns={"IN": "InQuantity", "OUT": "OutQuantity"})
        return result[["Category", "InQuantity", "OutQuantity"]].sort_values("Category").reset_index(drop=True)

    def high_outbound_products(self, df, n):
        result = (
            df[df["MovementType"] == "OUT"]
            .groupby(["ProductID", "ProductName"])["Quantity"]
            .sum()
            .reset_index(name="TotalOutQuantity")
        )
        result = result[result["TotalOutQuantity"] > n]
        return result.sort_values(["TotalOutQuantity", "ProductID"], ascending=[False, True]).reset_index(drop=True)

if __name__ == "__main__":
    products = [
        ["P101", "Keyboard", "Electronics", 1200],
        ["P102", "Chair", "Furniture", 3500],
        ["P103", "Mouse", "Electronics", 600],
    ]
    movements = [
        ["M1", "P101", "IN", 20, "2026-08-01"],
        ["M2", "P101", "OUT", 12, "2026-08-02"],
        ["M3", "P102", "OUT", 7, "2026-08-02"],
        ["M4", "P103", "IN", 15, "2026-08-03"],
        ["M5", "P103", "OUT", 4, "2026-08-04"],
    ]
    a = InventoryMovementAnalyzer()
    products_df = a.create_product_df(products)
    movements_df = a.create_movement_df(movements)
    merged = a.merge_product_movements(products_df, movements_df)

    print("1. create_product_df")
    print(products_df)
    print("\n2. create_movement_df")
    print(movements_df)
    print("\n3. merge_product_movements")
    print(merged)
    print("\n4. add_movement_value")
    print(a.add_movement_value(merged))
    print("\n5. category_movement_summary")
    print(a.category_movement_summary(merged))
    print("\n6. high_outbound_products")
    print(a.high_outbound_products(merged, 5))
