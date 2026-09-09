import numpy as np

class PriceAdjustmentAnalyzer:
    def create_price_array(self, prices: list) -> np.ndarray:
        return np.array(prices, dtype=float)

    def limit_price_range(
        self, arr: np.ndarray, minimum: float, maximum: float
    ) -> np.ndarray:
        return np.clip(arr, minimum, maximum)

    def apply_tax(self, arr: np.ndarray, tax_percent: float) -> np.ndarray:
        return np.round(arr * (1 + tax_percent / 100), 2)

    def discount_expensive_items(
        self, arr: np.ndarray, threshold: float, discount_percent: float
    ) -> np.ndarray:
        return np.round(
            np.where(
                arr >= threshold,
                arr * (1 - discount_percent / 100),
                arr
            ),
            2
        )

    def sort_prices_descending(self, arr: np.ndarray) -> np.ndarray:
        return np.sort(arr)[::-1]

    def price_spread(self, arr: np.ndarray) -> float:
        if arr.size == 0:
            return 0.0
        return float(np.max(arr) - np.min(arr))


if __name__ == "__main__":
    analyzer = PriceAdjustmentAnalyzer()

    prices = analyzer.create_price_array([35, 99.99, 175, 260])
    print("Price array:", prices)
    print("Limited range:", analyzer.limit_price_range(prices, 50, 200))
    print("With 18% tax:", analyzer.apply_tax(prices, 18))
    print("After 15% expensive-item discount:", analyzer.discount_expensive_items(
        prices, 100, 15
    ))
    print("Descending prices:", analyzer.sort_prices_descending(prices))
    print("Price spread:", analyzer.price_spread(prices))

    print("Threshold boundary:", analyzer.discount_expensive_items(
        np.array([100.0, 120.0]), 100, 10
    ))
    print("Empty spread:", analyzer.price_spread(np.array([])))
