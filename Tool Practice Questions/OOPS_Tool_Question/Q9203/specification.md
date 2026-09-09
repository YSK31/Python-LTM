# Q9203

## Problem Statement

Implement a coupon balance tracker using an instance dictionary mapping customer IDs to coupon points.

## Class

`CouponBalanceTracker`

## Operations

### 1. Add Coupon Points
`add_coupon_points(customer_id: str, points: int) -> dict`

Add points to an existing customer or create the customer with the supplied point balance. Return the coupons dictionary.

### 2. Redeem Points
`redeem_points(customer_id: str, points: int) -> dict`

Redeem points from a customer. If the customer is missing or has fewer points than requested, raise `ValueError("Insufficient coupon points")`. Return the coupons dictionary.

### 3. Transfer Balance
`transfer_balance(old_customer_id: str, new_customer_id: str) -> dict`

Move the old customer's complete balance to the new customer, adding to an existing destination balance when present, and remove the old customer. If the old customer does not exist, return the current dictionary unchanged.

### 4. Active Customers
`active_customers() -> list`

Return customer IDs whose coupon balance is greater than zero.

## Source Note

This specification is derived directly from the GitHub solution used for this practice question. No external requirements are added.
