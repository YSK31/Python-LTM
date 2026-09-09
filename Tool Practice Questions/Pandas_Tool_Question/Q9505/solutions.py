import pandas as pd

class FleetTripAnalyzer:
    def create_trip_df(self, data):
        return pd.DataFrame(data, columns=["TripID", "Driver", "VehicleType", "TripDate", "DistanceKm", "FuelLitres"])

    def add_fuel_efficiency(self, df):
        result = df.copy()
        result["EfficiencyKmPerL"] = (result["DistanceKm"] / result["FuelLitres"]).round(2)
        return result

    def add_distance_band(self, df):
        result = df.copy()
        result["DistanceBand"] = "Short"
        result.loc[result["DistanceKm"].between(50, 150, inclusive="both"), "DistanceBand"] = "Medium"
        result.loc[result["DistanceKm"] > 150, "DistanceBand"] = "Long"
        return result

    def driver_trip_summary(self, df):
        result = df.groupby("Driver").agg(
            TripCount=("TripID", "size"),
            TotalDistanceKm=("DistanceKm", "sum"),
            AverageFuelLitres=("FuelLitres", "mean")
        ).reset_index()
        result["AverageFuelLitres"] = result["AverageFuelLitres"].round(2)
        return result.sort_values("Driver").reset_index(drop=True)

    def vehicle_distance_table(self, df):
        result = df.pivot_table(
            index="VehicleType",
            columns="DistanceBand",
            values="DistanceKm",
            aggfunc="sum",
            fill_value=0
        ).reindex(columns=["Short", "Medium", "Long"], fill_value=0).reset_index()
        return result.sort_values("VehicleType").reset_index(drop=True)

    def top_efficient_trips(self, df, n):
        result = df.sort_values(
            ["EfficiencyKmPerL", "TripID"], ascending=[False, True]
        )[["TripID", "Driver", "EfficiencyKmPerL"]]
        return result.head(n).reset_index(drop=True)

if __name__ == "__main__":
    data = [
        ["T1", "Ravi", "Van", "2026-08-01", 120, 8],
        ["T2", "Asha", "Bike", "2026-08-02", 40, 2],
        ["T3", "Ravi", "Van", "2026-08-03", 150, 10],
        ["T4", "Dev", "Truck", "2026-08-04", 200, 20],
    ]
    a = FleetTripAnalyzer()
    df = a.create_trip_df(data)
    efficient = a.add_fuel_efficiency(df)
    banded = a.add_distance_band(df)
    both = a.add_distance_band(efficient)

    print("1. create_trip_df")
    print(df)
    print("\n2. add_fuel_efficiency")
    print(efficient)
    print("\n3. add_distance_band")
    print(banded)
    print("\n4. driver_trip_summary")
    print(a.driver_trip_summary(df))
    print("\n5. vehicle_distance_table")
    print(a.vehicle_distance_table(both))
    print("\n6. top_efficient_trips")
    print(a.top_efficient_trips(both, 3))
