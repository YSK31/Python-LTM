import numpy as np

class SensorAnalyzer:
    def create_sensor_array(self, sensor_values: list) -> np.ndarray:
        return np.array(sensor_values, dtype=float)

    def validate_sensor_array(self, sensor_array: np.ndarray) -> bool:
        return sensor_array.size > 0 and np.all(sensor_array > 0)

    def compute_sensor_statistics(self, sensor_array: np.ndarray) -> tuple:
        total = float(np.sum(sensor_array))
        average = round(float(np.mean(sensor_array)), 1)
        maximum = float(np.max(sensor_array))
        return total, average, maximum

    def filter_extreme_readings(self, sensor_array: np.ndarray) -> np.ndarray:
        arr = sensor_array.astype(float)
        return np.where(arr >= 50.0, arr * 0.9, arr)

    def label_high_sensors(self, sensor_array: np.ndarray) -> np.ndarray:
        mean = np.mean(sensor_array)
        return np.where(sensor_array > mean, "High", "Normal")

    def format_sensor_readings(self, sensor_array: np.ndarray) -> np.ndarray:
        return np.array([f"{x:.2f} units" for x in sensor_array])


if __name__ == "__main__":
    analyzer = SensorAnalyzer()

    readings = analyzer.create_sensor_array([24.5, 52.0, 68.75, 31.25])
    print("Sensor array:", readings)
    print("Valid:", analyzer.validate_sensor_array(readings))
    print("Statistics:", analyzer.compute_sensor_statistics(readings))
    print("Filtered readings:", analyzer.filter_extreme_readings(readings))
    print("High/Normal labels:", analyzer.label_high_sensors(readings))
    print("Formatted readings:", analyzer.format_sensor_readings(readings))

    print("Empty valid:", analyzer.validate_sensor_array(np.array([])))
    print("Boundary filtering:", analyzer.filter_extreme_readings(np.array([49.9, 50.0, 70.0])))
