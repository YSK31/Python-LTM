class MobileDataUsageSystem:
    def __init__(self):
        self.customers = {}
    
    def add_customer(self, customer_id, name, plan_name, data_used):
        if customer_id in self.customers:
            raise ValueError("Customer already exists")
        self.customers[customer_id] = {"name": name, "plan_name": plan_name, "data_used": data_used, "status": "Active"}
        return self.customers
    
    def update_data_usage(self, customer_id, new_usage):
        if customer_id not in self.customers:
            raise KeyError("Customer not found")
        self.customers[customer_id]["data_used"] = new_usage
        return self.customers
    
    def get_customer_details(self, customer_id):
        if customer_id not in self.customers:
            raise KeyError("Customer not found")
        return self.customers[customer_id]

    def get_high_data_users(self, usage_threshold):
        high_data_users = []
        for key, value in self.customers.items():
            if value["data_used"] >= usage_threshold:
                high_data_users.append(key)
        return high_data_users