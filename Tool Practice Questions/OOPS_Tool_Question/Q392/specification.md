# Q392

## Problem Statement

Implement a supply-chain inventory tracker using a class-level dictionary stored on the instance.

## Class

`SupplyChainInventory`

## Operations

### 1. Add Product
`add_product(product_id: str, quantity: int) -> dict`

Add the quantity to an existing product or create the product with the supplied quantity. Return the inventory dictionary.

### 2. Fulfill Order
`fulfill_order(product_id: str, quantity: int) -> dict`

Reduce the product stock by the requested quantity. If the product is missing or the available stock is insufficient, raise `ValueError("Insufficient Stock")`. Return the inventory dictionary.

### 3. Restock Return
`restock_return(product_id: str, quantity: int) -> dict`

Add returned stock to an existing product or create the product with the supplied quantity. Return the inventory dictionary.

### 4. List Available Products
`list_available_products() -> list`

Return product IDs whose current stock is greater than zero.

## Source Note

This specification is derived directly from the solution code because the supplied question package contained an empty `specification.md`.
