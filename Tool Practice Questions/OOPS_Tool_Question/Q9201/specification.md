Campus Parking Lot Management System

**Question Code:**: Q9201

**Difficulty Level**: Easy

**Technology**: Python OOP

**Total Marks**: 10

**Assessment SOP**: Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.

## Problem Statement

A campus parking office manages vehicle parking slots. Each vehicle record is stored using vehicle number as the key, and the value is a dictionary containing owner, slot, and status. The system should add vehicles, update parking slots, fetch vehicle details, and list vehicles parked in a zone.

## Class Creation

class ParkingLotSystem:

## Constructor

def __init__(self):
 self.vehicles = {}

## Operations

1. Add Vehicle

Function Prototype
def add_vehicle(self, vehicle_no: str, owner: str, slot: str) -> dict:

Example Input
system.add_vehicle("KA22MN4501", "Dev", "C-18")

Expected Output
{"KA22MN4501": {"owner": "Dev", "slot": "C-18", "status": "Parked"}}

## Implementation Flow

• Check whether vehicle_no already exists in self.vehicles.
• If the vehicle already exists, raise ValueError("Vehicle already exists").
• Otherwise add a nested dictionary with owner, slot, and status as "Parked".
• Return self.vehicles.

## Hidden Test Focus

• Duplicate vehicle number must raise only ValueError("Vehicle already exists").

2. Update Slot

Function Prototype
def update_slot(self, vehicle_no: str, new_slot: str) -> dict:

Example Input
system.update_slot("KA22MN4501", "C-22")

Expected Output
{"KA22MN4501": {"owner": "Dev", "slot": "C-22", "status": "Parked"}}

## Implementation Flow

• Check whether vehicle_no exists in self.vehicles.
• If missing, raise KeyError("Vehicle not found").
• Update only the slot value.
• Do not change owner or status.
• Return self.vehicles.

## Hidden Test Focus

• Missing vehicle update must raise only KeyError("Vehicle not found").

3. Get Vehicle Details

Function Prototype
def get_vehicle_details(self, vehicle_no: str) -> dict:

Example Input
system.get_vehicle_details("KA22MN4501")

Expected Output
{"owner": "Dev", "slot": "C-18", "status": "Parked"}

## Implementation Flow

• Check whether vehicle_no exists in self.vehicles.
• If missing, raise KeyError("Vehicle not found").
• Return the nested vehicle dictionary.

4. Vehicles by Zone

Function Prototype
def vehicles_by_zone(self, zone_prefix: str) -> list:

Example Input
system.vehicles_by_zone("C")

Expected Output
["KA22MN4501", "TN10PQ7700"]

## Implementation Flow

• Declare an empty list.
• Iterate through self.vehicles using an explicit loop.
• Check whether each vehicle slot starts with zone_prefix using startswith().
• Append matching vehicle numbers to the result list.
• Return the result list.

## Driver and SOP Notes

Assessment behavior:
• Each test case has its own setup data; no function depends on another function passing.
• The driver overwrites test_report.log on every execution using latest run data only.
• The report lists individual pass/fail/crash results and error details only.
• No total score, marks obtained, final score, or percentage is printed at the end.
• OOP questions are easy category with total 10 marks.
• Only 2 hidden test cases are used; each hidden test validates one function only.
