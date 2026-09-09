class GymWorkoutSystem:
    def __init__(self):
        self.members = {}

    def add_member(self, member_id, name, workout_type, workout_minutes):
        if member_id in self.members:
            raise ValueError("Member already exists")
        self.members[member_id] = {"name": name, "workout_type": workout_type, "workout_minutes": workout_minutes, "status": "Active"}
        return self.members

    def update_workout_minutes(self, member_id, new_minutes):
        if member_id not in self.members:
            raise KeyError("Member not found")
        self.members[member_id]["workout_minutes"] = new_minutes
        return self.members

    def get_member_details(self, member_id):
        if member_id not in self.members:
            raise KeyError("Member not found")
        return self.members[member_id]

    def get_active_members(self, minimum_minutes):
        active_members = []
        for key, val in self.members.items():
            if val["workout_minutes"] >= minimum_minutes:
                active_members.append(key)
        return active_members


if __name__ == "__main__":
    system = GymWorkoutSystem()

    print("Add member:", system.add_member("M101", "Ravi", "Strength", 45))
    print("Add second member:", system.add_member("M102", "Anu", "Cardio", 70))
    print("Update workout minutes:", system.update_workout_minutes("M101", 60))
    print("Member details:", system.get_member_details("M101"))
    print("Members with >= 60 minutes:", system.get_active_members(60))

    try:
        system.add_member("M101", "Ravi", "Strength", 30)
    except ValueError as e:
        print("Duplicate member test:", e)

    try:
        system.get_member_details("M999")
    except KeyError as e:
        print("Missing member test:", e)
