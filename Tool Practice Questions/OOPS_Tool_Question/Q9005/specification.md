# Q9005

## Problem Statement

Implement a mobile data usage management system using an instance dictionary of customer records.

## Class

`MobileDataUsageSystem`

## Operations

### 1. Add Customer
`add_customer(customer_id, name, plan_name, data_used)`

Create an active customer record. Raise `ValueError("Customer already exists")` for a duplicate customer ID. Return the customers dictionary.

### 2. Update Data Usage
`update_data_usage(customer_id, new_usage)`

Update data usage for an existing customer. Raise `KeyError("Customer not found")` when the customer ID is missing. Return the customers dictionary.

### 3. Get Customer Details
`get_customer_details(customer_id)`

Return the customer record. Raise `KeyError("Customer not found")` when the customer ID is missing.

### 4. Get High Data Users
`get_high_data_users(usage_threshold)`

Return customer IDs whose data usage is greater than or equal to the supplied threshold.

## Source Note

This specification is derived directly from the GitHub solution used for this practice question. No external requirements are added.
