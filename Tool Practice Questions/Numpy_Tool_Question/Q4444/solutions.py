import numpy as np

class WaterQualityAnalyzer:
    def create_quality_array(self, readings: list) -> np.ndarray:
        return np.array(readings)

    def validate_quality_array(self, arr: np.ndarray) -> bool:
        return arr.size > 0 and np.all(arr >= 0)

    def compute_quality_statistics(self, arr: np.ndarray) -> tuple:
        return (np.sum(arr), np.mean(arr), np.max(arr))

    def filter_extreme_levels(self, arr: np.ndarray) -> np.ndarray:
        return np.where(arr >= 100, arr * 0.9, arr).astype(float)

    def label_high_pollution(self, arr: np.ndarray) -> np.ndarray:
        return np.where(arr > 75, "High", "Normal")

    def format_quality_readings(self, arr: np.ndarray) -> np.ndarray:
        return np.array([f"{value:.2f} ppm" for value in arr])


if __name__ == "__main__":
    analyzer = WaterQualityAnalyzer()

    readings = analyzer.create_quality_array([28.5, 82.25, 105.0, 140.75])
    print("Quality array:", readings)
    print("Valid:", analyzer.validate_quality_array(readings))
    print("Statistics:", analyzer.compute_quality_statistics(readings))
    print("Filtered extremes:", analyzer.filter_extreme_levels(readings))
    print("Pollution labels:", analyzer.label_high_pollution(readings))
    print("Formatted readings:", analyzer.format_quality_readings(readings))

    print("Empty valid:", analyzer.validate_quality_array(np.array([])))
    print("Negative valid:", analyzer.validate_quality_array(np.array([10, -2, 30])))
