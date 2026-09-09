import numpy as np

def create_watch_array(watch_data: list) -> np.ndarray:
    return np.array(watch_data, dtype=np.int64)

def validate_watch_array(watch_array: np.ndarray) -> bool:
    if watch_array.size == 0:
        return False
    if not np.issubdtype(watch_array.dtype, np.number):
        return False
    return bool(np.all(watch_array >= 0))

def compute_watch_metrics(watch_array: np.ndarray) -> tuple:
    return (
        int(np.sum(watch_array)),
        round(float(np.mean(watch_array)), 2),
        int(np.max(watch_array)),
    )

def categorize_watch_levels(watch_array: np.ndarray) -> np.ndarray:
    return np.where(
        watch_array < 1000,
        "Low Watch",
        np.where(watch_array < 3000, "Medium Watch", "High Watch")
    )

def longest_watch_growth_streak(watch_array: np.ndarray) -> int:
    if watch_array.size == 0:
        return 0
    if watch_array.size == 1:
        return 1

    max_streak = 1
    current_streak = 1

    for i in range(1, len(watch_array)):
        if watch_array[i] > watch_array[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak

def format_watch_minutes(watch_array: np.ndarray) -> np.ndarray:
    return np.array([f"{value:,}" for value in watch_array])


if __name__ == "__main__":
    watch = create_watch_array([850, 1250, 1800, 1600, 3200, 4100])
    print("Watch array:", watch)
    print("Valid:", validate_watch_array(watch))
    print("Metrics:", compute_watch_metrics(watch))
    print("Levels:", categorize_watch_levels(watch))
    print("Longest growth streak:", longest_watch_growth_streak(watch))
    print("Formatted:", format_watch_minutes(watch))

    print("Boundary levels:", categorize_watch_levels(
        np.array([999, 1000, 2999, 3000])
    ))
    print("Empty valid:", validate_watch_array(np.array([], dtype=int)))
    print("Non-numeric valid:", validate_watch_array(np.array(["900", "1200"])))
