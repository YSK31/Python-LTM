import numpy as np

class ElectricityUsageAnalyzer:
    def create_usage_array(self, readings: list) -> np.ndarray:
        return np.array(readings, dtype=float)

    def validate_usage_array(self, arr: np.ndarray) -> bool:
        return arr.size > 0 and np.all(arr >= 0)

    def daily_usage_change(self, arr: np.ndarray) -> np.ndarray:
        return np.diff(arr)

    def peak_usage_indices(self, arr: np.ndarray, threshold: float) -> np.ndarray:
        return np.where(arr > threshold)[0]

    def normalize_usage(self, arr: np.ndarray) -> np.ndarray:
        if arr.size == 0:
            return np.array([], dtype=float)
        minimum = np.min(arr)
        maximum = np.max(arr)
        if minimum == maximum:
            return np.zeros_like(arr, dtype=float)
        return np.round((arr - minimum) / (maximum - minimum), 3)

    def three_day_moving_average(self, arr: np.ndarray) -> np.ndarray:
        if arr.size < 3:
            return np.array([], dtype=float)
        return np.round(
            np.convolve(arr, np.ones(3) / 3, mode="valid"),
            2
        )


if __name__ == "__main__":
    analyzer = ElectricityUsageAnalyzer()

    usage = analyzer.create_usage_array([6.5, 9.0, 7.5, 12.0, 15.5])
    print("Usage array:", usage)
    print("Valid:", analyzer.validate_usage_array(usage))
    print("Daily changes:", analyzer.daily_usage_change(usage))
    print("Peak indices above 10:", analyzer.peak_usage_indices(usage, 10))
    print("Normalized usage:", analyzer.normalize_usage(usage))
    print("Three-day moving average:", analyzer.three_day_moving_average(usage))

    print("Equal-value normalization:", analyzer.normalize_usage(
        np.array([4.0, 4.0, 4.0])
    ))
    print("Short moving average:", analyzer.three_day_moving_average(
        np.array([2.0, 4.0])
    ))
