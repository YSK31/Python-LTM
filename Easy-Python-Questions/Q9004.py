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