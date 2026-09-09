class ClinicQueueSystem:
    def __init__(self):
        self.queue_data = {}

    def add_department(self, department: str, waiting_count: int) -> dict:
        self.queue_data[department] = waiting_count
        return self.queue_data

    def update_waiting_count(self, department: str, new_count: int) -> dict:
        if department not in self.queue_data:
            raise KeyError("Department not found")
        self.queue_data[department] = new_count
        return self.queue_data

    def crowded_departments(self, threshold: int) -> dict:
        result = {}
        for key, val in self.queue_data.items():
            if val > threshold:
                result[key] = val
        return result

    def assign_queue_actions(self) -> dict:
        result = {}
        for key, val in self.queue_data.items():
            if val > 60:
                result[key] = "Open Extra Counter"
            elif val >= 25 and val <= 60:
                result[key] = "Normal Queue"
            else:
                result[key] = "Fast Queue"
        return result


if __name__ == "__main__":
    system = ClinicQueueSystem()

    print("Add department:", system.add_department("General", 18))
    print("Add department 2:", system.add_department("ENT", 25))
    print("Add department 3:", system.add_department("Ortho", 60))
    print("Add department 4:", system.add_department("Cardio", 61))
    print("Update waiting count:", system.update_waiting_count("General", 30))
    print("Crowded departments > 25:", system.crowded_departments(25))
    print("Queue actions:", system.assign_queue_actions())

    try:
        system.update_waiting_count("Unknown", 10)
    except KeyError as e:
        print("Missing department test:", e)
