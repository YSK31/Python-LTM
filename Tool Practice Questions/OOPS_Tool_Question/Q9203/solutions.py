class CouponBalanceTracker:
    def __init__(self):
        self.coupons = {}

    def add_coupon_points(self, customer_id: str, points: int) -> dict:
        if customer_id in self.coupons:
            self.coupons[customer_id] += points
        else:
            self.coupons[customer_id] = points
        return self.coupons

    def redeem_points(self, customer_id: str, points: int) -> dict:
        if customer_id not in self.coupons:
            raise ValueError("Insufficient coupon points")
        if self.coupons[customer_id] < points:
            raise ValueError("Insufficient coupon points")
        self.coupons[customer_id] -= points
        return self.coupons

    def transfer_balance(self, old_customer_id: str, new_customer_id: str) -> dict:
        if old_customer_id not in self.coupons:
            return self.coupons
        old_balance = self.coupons[old_customer_id]
        if new_customer_id in self.coupons:
            self.coupons[new_customer_id] += old_balance
        else:
            self.coupons[new_customer_id] = old_balance
        del self.coupons[old_customer_id]
        return self.coupons

    def active_customers(self) -> list:
        active_cust = []
        for key,val in self.coupons.items():
            if val > 0:
                active_cust.append(key)
        return active_cust


if __name__ == "__main__":
    tracker = CouponBalanceTracker()

    print("Add points:", tracker.add_coupon_points("C501", 120))
    print("Add more points:", tracker.add_coupon_points("C501", 30))
    print("Redeem points:", tracker.redeem_points("C501", 50))
    tracker.add_coupon_points("C502", 40)
    print("Transfer balance:", tracker.transfer_balance("C501", "C502"))
    print("Active customers:", tracker.active_customers())

    try:
        tracker.redeem_points("C502", 500)
    except ValueError as e:
        print("Insufficient points test:", e)

    print("Missing transfer test:", tracker.transfer_balance("C999", "C503"))
