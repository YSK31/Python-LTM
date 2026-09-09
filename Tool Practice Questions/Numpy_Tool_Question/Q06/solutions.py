import numpy as np

class NumpyArrayAnalyzer:
    def create_order_array(self, amounts):
        return np.array(amounts, dtype=float)

    def validate_order_array(self, order_array):
        return order_array.size > 0 and np.all(order_array >= 0)

    def apply_discount(self, order_array):
        return np.where(order_array >= 150.0, order_array * 0.9, order_array)

    def format_order_amounts(self, order_array):
        return np.array([f"${amount:.2f}" for amount in order_array], dtype=object)

    def compute_order_summary(self, order_array):
        return (
            float(np.sum(order_array)),
            float(np.mean(order_array)),
            float(np.max(order_array)),
        )

    def flag_high_value_orders(self, order_array, threshold=150.0):
        return np.where(order_array >= threshold, "High", "Normal")

    def create_stock_array(self, changes):
        return np.array(changes)

    def validate_stock_array(self, changes):
        return changes.size > 0 and np.all((changes >= -10) & (changes <= 10))

    def compute_volatility(self, changes):
        ddof = 1 if changes.size > 1 else 0
        return (
            float(np.mean(changes)),
            float(np.std(changes, ddof=ddof)),
            float(np.max(changes)),
        )

    def flag_volatile_stocks(self, changes):
        return np.where(
            changes < 2,
            "Stable",
            np.where(changes <= 5, "Moderate Risk", "High Risk")
        )

    def longest_loss_streak(self, changes):
        max_streak = 0
        current_streak = 0

        for value in changes:
            if value < 0:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0

        return max_streak

    def format_stock_report(self, changes):
        return np.array([f"{change:.2f}%" for change in changes])

    def create_sequential_array(self, start, stop, step=1):
        return np.arange(start, stop, step)

    def compute_elementwise_square(self, arr):
        return np.square(arr)

    def compute_statistics(self, arr):
        return (
            float(np.sum(arr)),
            float(np.mean(arr)),
            float(np.min(arr)),
            float(np.max(arr)),
        )

    def filter_above_threshold(self, arr, threshold):
        return arr[arr > threshold]

    def replace_negatives_with_zero(self, arr):
        return np.where(arr < 0, 0, arr)

    def normalize_array(self, arr):
        if arr.size == 0:
            return np.array([], dtype=float)
        minimum = np.min(arr)
        maximum = np.max(arr)
        if minimum == maximum:
            return np.zeros_like(arr, dtype=float)
        return (arr - minimum) / (maximum - minimum)

    def concatenate_arrays(self, a, b):
        return np.concatenate((a, b))

    def compute_dot_product(self, a, b):
        return float(np.dot(a, b))

    def get_unique_values(self, arr):
        return np.unique(arr)

    def sort_array(self, arr):
        return np.sort(arr)

    def count_nonzero(self, arr):
        return int(np.count_nonzero(arr))


if __name__ == "__main__":
    analyzer = NumpyArrayAnalyzer()

    orders = analyzer.create_order_array([80, 150, 220, 95])
    print("Order array:", orders)
    print("Orders valid:", analyzer.validate_order_array(orders))
    print("Discounted orders:", analyzer.apply_discount(orders))
    print("Formatted orders:", analyzer.format_order_amounts(orders))
    print("Order summary:", analyzer.compute_order_summary(orders))
    print("Order flags:", analyzer.flag_high_value_orders(orders))

    stocks = analyzer.create_stock_array([1.5, -3.0, 2.5, 7.0, -4.0, -2.0])
    print("Stock array:", stocks)
    print("Stocks valid:", analyzer.validate_stock_array(stocks))
    print("Volatility:", analyzer.compute_volatility(stocks))
    print("Stock risk:", analyzer.flag_volatile_stocks(stocks))
    print("Longest loss streak:", analyzer.longest_loss_streak(stocks))
    print("Stock report:", analyzer.format_stock_report(stocks))

    data = np.array([-4, 0, 2, 5, 8])
    print("Sequential array:", analyzer.create_sequential_array(2, 10, 2))
    print("Squares:", analyzer.compute_elementwise_square(data))
    print("Statistics:", analyzer.compute_statistics(data))
    print("Above 3:", analyzer.filter_above_threshold(data, 3))
    print("Negatives replaced:", analyzer.replace_negatives_with_zero(data))
    print("Normalized:", analyzer.normalize_array(np.array([10.0, 20.0, 30.0])))
    print("Concatenated:", analyzer.concatenate_arrays(np.array([1, 2]), np.array([3, 4])))
    print("Dot product:", analyzer.compute_dot_product(np.array([1, 2, 3]), np.array([4, 5, 6])))
    print("Unique:", analyzer.get_unique_values(np.array([3, 1, 3, 2, 1])))
    print("Sorted:", analyzer.sort_array(np.array([7, 2, 5, 1])))
    print("Non-zero count:", analyzer.count_nonzero(np.array([0, 2, 0, 5, 7])))

    print("Empty order valid:", analyzer.validate_order_array(np.array([])))
    print("Stock boundary valid:", analyzer.validate_stock_array(np.array([-10, 0, 10])))
    print("Equal normalization:", analyzer.normalize_array(np.array([5.0, 5.0, 5.0])))
