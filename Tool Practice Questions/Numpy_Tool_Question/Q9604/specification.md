# **Electric Scooter Battery Cycle Analyzer**

## **Question Code: Q9604**
**Difficulty Level:** Medium
**Technology:** NumPy
**Total Marks:** 20

## **Problem Statement**
A scooter fleet records battery percentage after consecutive trip checkpoints. Build a NumPy analyzer to inspect charge movement, calculate cumulative drain, find recharge events, replace invalid readings, and determine the largest single drop.

# **Class Creation**
```python
class BatteryCycleAnalyzer:
```

## **1. Create Battery Array**
```python
def create_battery_array(self, levels: list) -> np.ndarray:
```
Return a float NumPy array in the same order.

## **2. Validate Battery Levels**
```python
def validate_battery_levels(self, arr: np.ndarray) -> bool:
```
The array must be non-empty and every battery level must be from 0 to 100 inclusive.

## **3. Checkpoint Changes**
```python
def checkpoint_changes(self, arr: np.ndarray) -> np.ndarray:
```
Return the difference between each checkpoint and the previous checkpoint. Example: `[90, 75, 80, 50]` -> `[-15, 5, -30]`.

## **4. Total Battery Drain**
```python
def total_battery_drain(self, arr: np.ndarray) -> float:
```
Calculate total drain by adding only decreases between consecutive checkpoints. Increases represent recharging and must not reduce the drain total.

Example: `[90, 70, 80, 50]` has drain `20 + 30 = 50.0`.

## **5. Recharge Event Indices**
```python
def recharge_event_indices(self, arr: np.ndarray) -> np.ndarray:
```
Return the zero-based indices of checkpoints where the battery level is greater than the immediately previous checkpoint. For `[90, 70, 80, 60, 75]`, return `[2, 4]`.

## **6. Largest Single Drop**
```python
def largest_single_drop(self, arr: np.ndarray) -> float:
```
Return the largest decrease between two consecutive checkpoints as a positive float. If fewer than 2 readings exist, return `0.0`. If there is no decrease, return `0.0`.
