# Q395

## Problem Statement

Implement an event-registration tracker using a dictionary stored on the instance.

## Class

`EventRegistrationTracker`

## Operations

### 1. Register Participant
`register_participant(event_id: str, count: int) -> dict`

Add the participant count to an existing event or create the event with the supplied count. Return the events dictionary.

### 2. Cancel Participant
`cancel_participant(event_id: str, count: int) -> dict`

Subtract the participant count from an event. If the event is missing or the registered count is smaller than the requested cancellation, raise `ValueError("Cannot cancel more participants than registered")`. Return the events dictionary.

### 3. Reschedule Event
`reschedule_event(old_event_id: str, new_event_id: str) -> dict`

When the old event exists, move its participant count to the new event, adding to the new event if it already exists, and remove the old event. When the old event does not exist, return the current dictionary unchanged.

### 4. Get Active Events
`get_active_events() -> list`

Return event IDs whose participant count is greater than zero.

## Source Note

This specification is derived directly from the solution code because the supplied question package contained an empty `specification.md`.
