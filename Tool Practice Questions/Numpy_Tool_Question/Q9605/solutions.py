import numpy as np

class ParcelWeightAnalyzer:
    def create_weight_array(self, weights: list) -> np.ndarray:
        return np.array(weights, dtype=float)

    def combine_weight_batches(self, first: np.ndarray, second: np.ndarray) -> np.ndarray:
        return np.concatenate((first, second))

    def unique_weight_counts(self, arr: np.ndarray) -> tuple:
        return np.unique(arr, return_counts=True)

    def round_to_half_kg(self, arr: np.ndarray) -> np.ndarray:
        return np.round(arr * 2) / 2

    def weights_within_range(
        self, arr: np.ndarray, minimum: float, maximum: float
    ) -> np.ndarray:
        return arr[(arr >= minimum) & (arr <= maximum)]

    def closest_weight_index(self, arr: np.ndarray, target: float) -> int:
        if arr.size == 0:
            return -1
        return int(np.argmin(np.abs(arr - target)))


if __name__ == "__main__":
    analyzer = ParcelWeightAnalyzer()

    first = analyzer.create_weight_array([1.2, 2.0, 3.5])
    second = analyzer.create_weight_array([2.0, 4.25, 5.0])
    combined = analyzer.combine_weight_batches(first, second)

    print("First batch:", first)
    print("Second batch:", second)
    print("Combined:", combined)
    print("Unique weights and counts:", analyzer.unique_weight_counts(combined))
    print("Rounded to 0.5 kg:", analyzer.round_to_half_kg(combined))
    print("Weights from 2 to 4.25 kg:", analyzer.weights_within_range(combined, 2, 4.25))
    print("Closest index to 3.0:", analyzer.closest_weight_index(combined, 3.0))

    print("Empty closest index:", analyzer.closest_weight_index(np.array([]), 2.0))
    print("Inclusive range:", analyzer.weights_within_range(
        np.array([1, 2, 3]), 1, 3
    ))
