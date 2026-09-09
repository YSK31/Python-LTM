# Q9004

## Problem Statement

Implement a parcel tracking system using an instance dictionary of parcel records.

## Class

`ParcelTrackingSystem`

## Operations

### 1. Add Parcel
`add_parcel(tracking_id, customer_name, destination, weight)`

Create a parcel record with status `"In Transit"`. Raise `ValueError("Parcel already exists")` for a duplicate tracking ID. Return the parcels dictionary.

### 2. Update Weight
`update_weight(tracking_id, new_weight)`

Update the weight of an existing parcel. Raise `KeyError("Parcel not found")` when the tracking ID is missing. Return the parcels dictionary.

### 3. Get Parcel Details
`get_parcel_details(tracking_id)`

Return the parcel record. Raise `KeyError("Parcel not found")` when the tracking ID is missing.

### 4. Get Heavy Parcels
`get_heavy_parcels(minimum_weight)`

Return tracking IDs whose weight is greater than or equal to the supplied minimum.

## Source Note

This specification is derived directly from the GitHub solution used for this practice question. No external requirements are added.
