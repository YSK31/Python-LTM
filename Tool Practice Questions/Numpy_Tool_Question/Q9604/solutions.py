import numpy as np

class BatteryCycleAnalyzer:
    def create_battery_array(self, levels: list) -> np.ndarray:
        return np.array(levels, dtype=float)

    def validate_battery_levels(self, arr: np.ndarray) -> bool:
        return arr.size > 0 and np.all((arr >= 0) & (arr <= 100))

    def checkpoint_changes(self, arr: np.ndarray) -> np.ndarray:
        return np.diff(arr)

    def total_battery_drain(self, arr: np.ndarray) -> float:
        changes = np.diff(arr)
        return float(np.sum(-changes[changes < 0]))

    def recharge_event_indices(self, arr: np.ndarray) -> np.ndarray:
        return np.where(np.diff(arr) > 0)[0] + 1

    def largest_single_drop(self, arr: np.ndarray) -> float:
        changes = np.diff(arr)
        if changes.size == 0:
            return 0.0
        drops = -changes[changes < 0]
        return float(np.max(drops)) if drops.size else 0.0


if __name__ == "__main__":
    analyzer = BatteryCycleAnalyzer()

    levels = analyzer.create_battery_array([96, 78, 84, 61, 72])
    print("Battery array:", levels)
    print("Valid:", analyzer.validate_battery_levels(levels))
    print("Changes:", analyzer.checkpoint_changes(levels))
    print("Total drain:", analyzer.total_battery_drain(levels))
    print("Recharge indices:", analyzer.recharge_event_indices(levels))
    print("Largest drop:", analyzer.largest_single_drop(levels))

    print("Boundary valid:", analyzer.validate_battery_levels(np.array([0, 100], dtype=float)))
    print("Invalid readings:", analyzer.validate_battery_levels(np.array([50, 101], dtype=float)))
    print("No drop:", analyzer.largest_single_drop(np.array([20, 30, 40], dtype=float)))
