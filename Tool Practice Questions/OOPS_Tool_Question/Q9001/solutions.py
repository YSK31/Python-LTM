class CafeteriaOrderSystem:
    def __init__(self):
        self.orders = {}

    def add_order(self, employee_id, name, meal_type, quantity):
        if employee_id in self.orders:
            raise ValueError("Order already exists")
        self.orders[employee_id] = {"name": name, "meal_type": meal_type, "quantity": quantity, "status": "Confirmed"}
        return self.orders

    def update_quantity(self, employee_id, new_quantity):
        if employee_id not in self.orders:
            raise KeyError("Order not found")
        self.orders[employee_id]["quantity"] = new_quantity
        return self.orders

    def get_order_details(self, employee_id):
        if employee_id not in self.orders:
            raise KeyError("Order not found")
        return self.orders[employee_id]

    def get_bulk_orders(self, minimum_quantity):
        emp_ids = []
        for key,keyval in self.orders.items():
            if keyval["quantity"] >= minimum_quantity:
                emp_ids.append(key)
        return emp_ids


if __name__ == "__main__":
    system = CafeteriaOrderSystem()

    print("Add order:", system.add_order("E101", "Arun", "Lunch", 2))
    print("Add second order:", system.add_order("E102", "Bala", "Dinner", 5))
    print("Update quantity:", system.update_quantity("E101", 4))
    print("Order details:", system.get_order_details("E101"))
    print("Bulk orders >= 4:", system.get_bulk_orders(4))

    try:
        system.add_order("E101", "Arun", "Lunch", 2)
    except ValueError as e:
        print("Duplicate order test:", e)

    try:
        system.get_order_details("E999")
    except KeyError as e:
        print("Missing order test:", e)
