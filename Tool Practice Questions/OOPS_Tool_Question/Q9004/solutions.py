class ParcelTrackingSystem:
    def __init__(self):
        self.parcels = {}

    def add_parcel(self, tracking_id, customer_name, destination, weight):
        if tracking_id in self.parcels:
            raise ValueError("Parcel already exists")
        self.parcels[tracking_id] = {"customer_name": customer_name, "destination": destination, "weight": weight, "status": "In Transit"}
        return self.parcels

    def update_weight(self, tracking_id, new_weight):
        if tracking_id not in self.parcels:
            raise KeyError("Parcel not found")
        self.parcels[tracking_id]["weight"] = new_weight
        return self.parcels

    def get_parcel_details(self, tracking_id):
        if tracking_id not in self.parcels:
            raise KeyError("Parcel not found")
        return self.parcels[tracking_id]

    def get_heavy_parcels(self, minimum_weight):
        heavy_parcels = []
        for key, value in self.parcels.items():
            if value["weight"] >= minimum_weight:
                heavy_parcels.append(key)
        return heavy_parcels


if __name__ == "__main__":
    system = ParcelTrackingSystem()

    print("Add parcel:", system.add_parcel("P101", "Rahul", "Chennai", 4.5))
    print("Add second parcel:", system.add_parcel("P102", "Sneha", "Hyderabad", 8.0))
    print("Update weight:", system.update_weight("P101", 6.0))
    print("Parcel details:", system.get_parcel_details("P101"))
    print("Heavy parcels >= 6 kg:", system.get_heavy_parcels(6))

    try:
        system.add_parcel("P101", "Rahul", "Chennai", 7.0)
    except ValueError as e:
        print("Duplicate parcel test:", e)

    try:
        system.get_parcel_details("P999")
    except KeyError as e:
        print("Missing parcel test:", e)
