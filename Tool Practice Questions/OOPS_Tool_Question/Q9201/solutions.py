class ParkingLotSystem:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle_no: str, owner: str, slot: str) -> dict:
        if vehicle_no in self.vehicles:
            raise ValueError("Vehicle already exists")
        self.vehicles[vehicle_no] = {"owner": owner, "slot": slot, "status": "Parked"}
        return self.vehicles

    def update_slot(self, vehicle_no: str, new_slot: str) -> dict:
        if vehicle_no not in self.vehicles:
            raise KeyError("Vehicle not found")
        self.vehicles[vehicle_no]["slot"] = new_slot
        return self.vehicles

    def get_vehicle_details(self, vehicle_no: str) -> dict:
        if vehicle_no not in self.vehicles:
            raise KeyError("Vehicle not found")
        return self.vehicles[vehicle_no]

    def vehicles_by_zone(self, zone_prefix: str) -> list:
        vehi = []
        for key,keyval in self.vehicles.items():
            if keyval["slot"].startswith(zone_prefix):
                vehi.append(key)
        return vehi


if __name__ == "__main__":
    system = ParkingLotSystem()

    print("Add vehicle:", system.add_vehicle("KA22MN4501", "Dev", "C-18"))
    print("Add vehicle 2:", system.add_vehicle("TN10PQ7700", "Meera", "C-22"))
    print("Add vehicle 3:", system.add_vehicle("AP09AB1234", "Ravi", "B-05"))
    print("Update slot:", system.update_slot("KA22MN4501", "C-25"))
    print("Vehicle details:", system.get_vehicle_details("KA22MN4501"))
    print("Vehicles in C zone:", system.vehicles_by_zone("C"))

    try:
        system.add_vehicle("KA22MN4501", "Dev", "C-30")
    except ValueError as e:
        print("Duplicate vehicle test:", e)

    try:
        system.update_slot("XX99", "A-01")
    except KeyError as e:
        print("Missing vehicle test:", e)
