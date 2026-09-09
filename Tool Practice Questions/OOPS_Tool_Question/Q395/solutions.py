class EventRegistrationTracker:
    def __init__(self):
        self.events = {}

    def register_participant(self, event_id: str, count: int) -> dict:
        if event_id in self.events:
            self.events[event_id] += count
        else:
            self.events[event_id] = count
        return self.events

    def cancel_participant(self, event_id: str, count: int) -> dict:
        if event_id not in self.events or self.events[event_id] < count:
            raise ValueError("Cannot cancel more participants than registered")
        self.events[event_id] -= count
        return self.events

    def reschedule_event(self, old_event_id: str, new_event_id: str) -> dict:
        if old_event_id not in self.events:
            return self.events
        count = self.events[old_event_id]
        if new_event_id in self.events:
            self.events[new_event_id] += count
        else:
            self.events[new_event_id] = count
        del self.events[old_event_id]
        return self.events

    def get_active_events(self) -> list:
        active_events = []
        for event_id, count in self.events.items():
            if count > 0:
                active_events.append(event_id)
        return active_events


if __name__ == "__main__":
    tracker = EventRegistrationTracker()

    print("Register:", tracker.register_participant("EVT100", 20))
    print("Register again:", tracker.register_participant("EVT100", 5))
    print("Cancel:", tracker.cancel_participant("EVT100", 5))
    print("Reschedule:", tracker.reschedule_event("EVT100", "EVT200"))
    print("Active events:", tracker.get_active_events())

    tracker.register_participant("EVT300", 10)
    tracker.register_participant("EVT301", 5)
    print("Merge reschedule:", tracker.reschedule_event("EVT301", "EVT300"))

    try:
        tracker.cancel_participant("EVT200", 999)
    except ValueError as e:
        print("Excess cancellation test:", e)
