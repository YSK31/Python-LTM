Delivery Fleet Trip Analyzer

**Question Code:**: Q9505

**Difficulty Level**: Medium

**Technology**: Pandas

**Total Marks**: 20

**Assessment SOP**: Independent test setup, latest-only report, no final score print

Open the Learnlytica assessment tool. Enter your Email address, enter the Question ID, and click Start Assessment. Open VSCode and implement only in solution.py. Run tests, validate, submit, and end assessment.
Sample inputs and expected outputs in this document are illustrative only and are intentionally different from actual visible and hidden driver test data.

## Problem Statement

A delivery company records completed vehicle trips. Each record contains trip ID, driver, vehicle type, trip date, distance, and fuel used. Build an analyzer that prepares the data, calculates fuel efficiency, classifies trip distance, creates driver summaries, produces a vehicle-distance pivot table, and lists the most efficient trips.

## Class Creation

class FleetTripAnalyzer:

## Constructor

def __init__(self):
 pass

## Operations

1. Create Trip DataFrame

Function Prototype
def create_trip_df(self, data: list) -> pd.DataFrame:
Input rows contain [TripID, Driver, VehicleType, TripDate, DistanceKm, FuelLitres].
Return columns TripID, Driver, VehicleType, TripDate, DistanceKm, FuelLitres in this exact order and preserve input row order.

2. Add Fuel Efficiency

Function Prototype
def add_fuel_efficiency(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Add EfficiencyKmPerL equal to DistanceKm divided by FuelLitres.
Round EfficiencyKmPerL to 2 decimal places.
Return all existing columns plus EfficiencyKmPerL.

3. Add Distance Band

Function Prototype
def add_distance_band(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Add DistanceBand using these rules:
DistanceKm less than 50 -> "Short"
DistanceKm from 50 through 150 inclusive -> "Medium"
DistanceKm greater than 150 -> "Long"
Return all existing columns plus DistanceBand.

4. Driver Trip Summary

Function Prototype
def driver_trip_summary(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Return one row per Driver with:
Driver, TripCount, TotalDistanceKm, AverageFuelLitres
Round AverageFuelLitres to 2 decimal places.
Sort Driver ascending and use a fresh 0-based index.

5. Vehicle Distance Table

Function Prototype
def vehicle_distance_table(self, df: pd.DataFrame) -> pd.DataFrame:
Requirement
Create a summary of total DistanceKm for every VehicleType across DistanceBand values.
Output columns must be exactly:
VehicleType, Short, Medium, Long
If a VehicleType has no trips in a distance band, use

0.
Sort VehicleType ascending and use a fresh 0-based index.

6. Top Efficient Trips

Function Prototype
def top_efficient_trips(self, df: pd.DataFrame, n: int) -> pd.DataFrame:
Requirement
Return the top n trips with the highest EfficiencyKmPerL.
Output columns:
TripID, Driver, EfficiencyKmPerL
Sort EfficiencyKmPerL descending and TripID ascending for ties. Use a fresh 0-based index.

## Driver and SOP Notes

• Each test case has its own setup data; no function depends on another function passing.
• The driver overwrites test_report.log on every execution using latest run data only.
• The report lists individual pass/fail/crash results and error details only.
• No total score, marks obtained, final score, or percentage is printed at the end.
