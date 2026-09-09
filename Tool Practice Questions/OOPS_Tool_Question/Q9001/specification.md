# Corporate Cafeteria Meal Order Management

**Difficulty:** Easy
**Marks:** 10
**Technology:** Python OOPs
**Domain:** Corporate Food / Cafeteria Operations

## Objective
Implement the class and exact methods below. Use a dictionary stored on the instance to maintain records.

## Class Name
`CafeteriaOrderSystem`

## Required Methods

### Task 1: `add_order()`
**Prototype:** `def add_order(self, employee_id, name, meal_type, quantity)`

Add a new meal order with status "Confirmed". Raise ValueError("Order already exists") if duplicate.

### Task 2: `update_quantity()`
**Prototype:** `def update_quantity(self, employee_id, new_quantity)`

Update quantity. Raise KeyError("Order not found") if missing.

### Task 3: `get_order_details()`
**Prototype:** `def get_order_details(self, employee_id)`

Return the order details. Raise KeyError("Order not found") if missing.

### Task 4: `get_bulk_orders()`
**Prototype:** `def get_bulk_orders(self, minimum_quantity)`

Return employee IDs where quantity >= minimum_quantity.

## Test Design
- 4 visible test cases
- 1 hidden test case
- Total marks: 10 (2 marks per test case)

## Constraints
- Use the exact class and method names.
- Do not use external libraries.
- Return values exactly as specified.
- Preserve insertion order when returning filtered ID lists.
