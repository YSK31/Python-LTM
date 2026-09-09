# **Parcel Weight Batch Analyzer**

## **Question Code: Q9605**
**Difficulty Level:** Medium  
**Technology:** NumPy  
**Total Marks:** 20

## **Problem Statement**
A logistics hub receives parcel weights from two scanning lanes. Build NumPy utilities to combine batches, find distinct weights and their frequencies, round weights to shipping increments, select parcels within a range, and locate the parcel closest to a target weight.

# **Class Creation**
```python
class ParcelWeightAnalyzer:
```

## **1. Create Weight Array**
```python
def create_weight_array(self, weights: list) -> np.ndarray:
```
Return a float NumPy array.

## **2. Combine Weight Batches**
```python
def combine_weight_batches(self, first: np.ndarray, second: np.ndarray) -> np.ndarray:
```
Combine the two arrays so all values from `first` appear before all values from `second`.

## **3. Unique Weight Counts**
```python
def unique_weight_counts(self, arr: np.ndarray) -> tuple:
```
Return `(unique_weights, counts)` as two NumPy arrays. Unique weights must be in ascending order and `counts` must show how many times each weight occurs.

Example: `[2.0, 1.5, 2.0, 3.0, 1.5]` -> `(array([1.5,2.0,3.0]), array([2,2,1]))`.

## **4. Round to Half Kilogram**
```python
def round_to_half_kg(self, arr: np.ndarray) -> np.ndarray:
```
Round each weight to the nearest 0.5 kg and return the resulting NumPy array.

Example: `[1.2, 1.3, 2.74, 2.76]` -> `[1.0, 1.5, 2.5, 3.0]`.

## **5. Weights Within Range**
```python
def weights_within_range(self, arr: np.ndarray, minimum: float, maximum: float) -> np.ndarray:
```
Return only weights between `minimum` and `maximum`, including both boundary values. Preserve original order.

## **6. Closest Weight Index**
```python
def closest_weight_index(self, arr: np.ndarray, target: float) -> int:
```
Return the zero-based index of the weight closest to `target`. If two values are equally close, return the lower index. Return `-1` for an empty array.
