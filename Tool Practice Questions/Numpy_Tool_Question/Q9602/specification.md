# **Retail Price Adjustment Analyzer**

## **Question Code: Q9602**
**Difficulty Level:** Medium  
**Technology:** NumPy  
**Total Marks:** 20

## **Assessment Instructions**
Open the Learnlytica assessment tool, enter your Email address and Question ID, and start the assessment. Implement only in `solution.py`. Run tests, validate, submit, and end the assessment.

# **Problem Statement**
An online retailer stores product prices in a NumPy array. The pricing team needs utilities to limit abnormal prices, apply a tax rate, reduce selected expensive items, sort final prices, and calculate price-range information.

# **Class Creation**
```python
class PriceAdjustmentAnalyzer:
```

## **1. Create Price Array**
```python
def create_price_array(self, prices: list) -> np.ndarray:
```
Create and return a float NumPy array.

## **2. Limit Price Range**
```python
def limit_price_range(self, arr: np.ndarray, minimum: float, maximum: float) -> np.ndarray:
```
Return a new array where values below `minimum` become `minimum`, values above `maximum` become `maximum`, and values inside the range remain unchanged.

Example: `[20, 55, 160]`, range 40 to 120 -> `[40, 55, 120]`.

## **3. Apply Tax**
```python
def apply_tax(self, arr: np.ndarray, tax_percent: float) -> np.ndarray:
```
Increase every price by the given percentage. Round to 2 decimal places.

## **4. Discount Expensive Items**
```python
def discount_expensive_items(self, arr: np.ndarray, threshold: float, discount_percent: float) -> np.ndarray:
```
Apply the discount only to prices **greater than or equal to** `threshold`; other prices stay unchanged. Round to 2 decimals.

## **5. Sort Prices Descending**
```python
def sort_prices_descending(self, arr: np.ndarray) -> np.ndarray:
```
Return a new NumPy array sorted from highest price to lowest price.

## **6. Price Spread**
```python
def price_spread(self, arr: np.ndarray) -> float:
```
Return the difference between the maximum and minimum price as a float. For an empty array, return `0.0`.
