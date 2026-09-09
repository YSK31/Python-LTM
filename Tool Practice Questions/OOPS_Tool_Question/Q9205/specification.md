Retail Coupon Balance Tracker

**Question Code:**: Q9205

**Difficulty Level**: Easy

**Technology**: Python OOP

**Total Marks**: 10

**Assessment SOP**: Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.

## Problem Statement

A retail store tracks coupon balances for customers. Each customer is stored using customer_id as the key and coupon points as the value. The system should add coupon points, redeem points, transfer balance, and list active customers.

## Class Creation

class CouponBalanceTracker:

## Constructor

def __init__(self):
 self.coupons = {}

## Operations

1. Add Coupon Points

Function Prototype
def add_coupon_points(self, customer_id: str, points: int) -> dict:

Example Input
system.add_coupon_points("C120", 75)

Expected Output
{"C120": 75}

## Implementation Flow

• If customer_id already exists, increase the existing coupon points.
• Otherwise create a new entry with the given points.
• Return self.coupons.

2. Redeem Points

Function Prototype
def redeem_points(self, customer_id: str, points: int) -> dict:

Example Input
system.redeem_points("C120", 20)

Expected Output
{"C120": 55}

## Implementation Flow

• Check whether customer_id exists and has enough points.
• If customer is missing or available points are less than points to redeem, raise ValueError("Insufficient coupon points").
• Subtract points from the customer balance.
• Return self.coupons.

## Hidden Test Focus

• Insufficient balance must raise only ValueError("Insufficient coupon points").

3. Transfer Customer Balance

Function Prototype
def transfer_balance(self, old_customer_id: str, new_customer_id: str) -> dict:

Example Input
system.transfer_balance("C120", "C130")

Expected Output
{"C130": 75}

## Implementation Flow

• If old_customer_id does not exist, return self.coupons unchanged.
• Store the old customer balance.
• If new_customer_id already exists, add the old balance to it.
• Otherwise create new_customer_id with the old balance.
• Delete old_customer_id using del.
• Return self.coupons.

## Hidden Test Focus

• Missing old customer should return the existing dictionary unchanged.

4. Active Customers

Function Prototype
def active_customers(self) -> list:

Example Input
system.active_customers()

Expected Output
["C120", "C130"]

## Implementation Flow

• Declare an empty list.
• Iterate through self.coupons using an explicit loop.
• Append customer IDs where coupon points are greater than

0.
• Return the list.

## Driver and SOP Notes

Assessment behavior:
• Each test case has its own setup data; no function depends on another function passing.
• The driver overwrites test_report.log on every execution using latest run data only.
• The report lists individual pass/fail/crash results and error details only.
• No total score, marks obtained, final score, or percentage is printed at the end.
• OOP questions are easy category with total 10 marks.
• Only 2 hidden test cases are used; each hidden test validates one function only.
