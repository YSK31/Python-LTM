# **Student Exam Score Analyzer**

## **Question Code: Q9603**
**Difficulty Level:** Medium  
**Technology:** NumPy  
**Total Marks:** 20

## **Problem Statement**
A training institute stores assessment scores for one batch. Build NumPy utilities to validate score limits, calculate percentile information, apply grace marks safely, find top-performing positions, and count pass results.

# **Class Creation**
```python
class ExamScoreAnalyzer:
```

## **1. Create Score Array**
```python
def create_score_array(self, scores: list) -> np.ndarray:
```
Return a NumPy array using integer values.

## **2. Validate Score Range**
```python
def validate_score_range(self, arr: np.ndarray) -> bool:
```
Return `False` if the array is empty. All scores must be between 0 and 100 inclusive.

## **3. Score Percentiles**
```python
def score_percentiles(self, arr: np.ndarray) -> tuple:
```
Return the 25th percentile, median (50th percentile), and 75th percentile, each rounded to 2 decimals, in that order.

## **4. Apply Grace Marks**
```python
def apply_grace_marks(self, arr: np.ndarray, grace: int) -> np.ndarray:
```
Add `grace` to every score, but no resulting score may exceed 100. Return an integer NumPy array.

## **5. Top Score Indices**
```python
def top_score_indices(self, arr: np.ndarray, n: int) -> np.ndarray:
```
Return the zero-based indices of the top `n` scores, ordered from highest score to lowest. If `n` is larger than the array size, return all indices. For equal scores, the lower original index should come first.

## **6. Count Passing Scores**
```python
def count_passing_scores(self, arr: np.ndarray, pass_mark: int) -> int:
```
Return how many scores are greater than or equal to `pass_mark`.
