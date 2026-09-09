class SupplyChainInventory:
    def __init__(self):
        self.inv = {}

    def add_product(self, product_id: str, quantity: int) -> dict:
        if product_id in self.inv:
            self.inv[product_id] += quantity
        else:
            self.inv[product_id] = quantity
        return self.inv

    def fulfill_order(self, product_id: str, quantity: int) -> dict:
        if product_id not in self.inv or self.inv[product_id] < quantity:
            raise ValueError("Insufficient Stock")
        self.inv[product_id] -= quantity
        return self.inv

    def restock_return(self, product_id: str, quantity: int) -> dict:
        if product_id in self.inv:
            self.inv[product_id] += quantity
        else:
            self.inv[product_id] = quantity
        return self.inv

    def list_available_products(self) -> list:
        return [product_id for product_id, stock in self.inv.items() if stock > 0]


if __name__ == "__main__":
    inventory = SupplyChainInventory()

    print("Add product:", inventory.add_product("PRD101", 50))
    print("Add more:", inventory.add_product("PRD101", 10))
    print("Fulfill order:", inventory.fulfill_order("PRD101", 20))
    print("Restock return:", inventory.restock_return("PRD101", 5))
    print("New product with zero stock:", inventory.restock_return("PRD102", 0))
    print("Available products:", inventory.list_available_products())

    try:
        inventory.fulfill_order("PRD101", 100)
    except ValueError as e:
        print("Insufficient stock test:", e)

    try:
        inventory.fulfill_order("PRD404", 5)
    except ValueError as e:
        print("Missing product test:", e)
