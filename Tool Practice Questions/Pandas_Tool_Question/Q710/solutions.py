import pandas as pd

class MatchDashboard:
    def create_match_df(self, match_data):
        return pd.DataFrame(match_data, columns=["Team", "Opponent", "Result", "Goals"])

    def team_goal_summary(self, df):
        result = df.groupby("Team")["Goals"].agg(["sum", "mean"]).reset_index()
        result.columns = ["Team", "Total Goals", "Average Goals"]
        return result

    def add_result_points(self, df):
        result = df.copy()
        result["Points"] = result["Result"].map({"Win": 3, "Draw": 1, "Loss": 0})
        return result

    def filter_high_scoring(self, df, n):
        return df[df["Goals"] > n].reset_index(drop=True)

    def compute_win_rate(self, df):
        total = df.groupby("Team").size()
        wins = df[df["Result"] == "Win"].groupby("Team").size()
        result = ((wins / total) * 100).fillna(0).round(1).reset_index()
        result.columns = ["Team", "Win Rate"]
        return result

    def top_teams_by_points(self, df, n):
        result = df.groupby("Team")["Points"].sum().reset_index()
        result = result.rename(columns={"Points": "Total Points"})
        return result.sort_values("Total Points", ascending=False).head(n).reset_index(drop=True)

if __name__ == "__main__":
    data = [
        ["Lions", "Tigers", "Win", 3],
        ["Lions", "Bears", "Draw", 2],
        ["Tigers", "Lions", "Loss", 1],
        ["Bears", "Lions", "Win", 4],
        ["Tigers", "Bears", "Win", 5],
    ]
    a = MatchDashboard()
    df = a.create_match_df(data)
    scored = a.add_result_points(df)

    print("1. create_match_df")
    print(df)
    print("\n2. team_goal_summary")
    print(a.team_goal_summary(df))
    print("\n3. add_result_points")
    print(scored)
    print("\n4. filter_high_scoring")
    print(a.filter_high_scoring(df, 2))
    print("\n5. compute_win_rate")
    print(a.compute_win_rate(df))
    print("\n6. top_teams_by_points")
    print(a.top_teams_by_points(scored, 2))
