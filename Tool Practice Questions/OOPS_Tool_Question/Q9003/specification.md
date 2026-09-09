# Q9003

## Problem Statement

Implement a gym workout management system using an instance dictionary of member records.

## Class

`GymWorkoutSystem`

## Operations

### 1. Add Member
`add_member(member_id, name, workout_type, workout_minutes)`

Create an active member record. Raise `ValueError("Member already exists")` for a duplicate member ID. Return the members dictionary.

### 2. Update Workout Minutes
`update_workout_minutes(member_id, new_minutes)`

Update workout minutes for an existing member. Raise `KeyError("Member not found")` when the member ID is missing. Return the members dictionary.

### 3. Get Member Details
`get_member_details(member_id)`

Return the member record. Raise `KeyError("Member not found")` when the member ID is missing.

### 4. Get Active Members
`get_active_members(minimum_minutes)`

Return member IDs whose workout minutes are greater than or equal to the supplied minimum.

## Source Note

This specification is derived directly from the GitHub solution used for this practice question. No external requirements are added.
