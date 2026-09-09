# Q9002

## Problem Statement

Implement a movie booking management system using an instance dictionary of booking records.

## Class

`MovieBookingSystem`

## Operations

### 1. Create Booking
`create_booking(booking_id, customer_name, movie_name, tickets)`

Create a booking with status `"Booked"`. Raise `ValueError("Booking already exists")` when the booking ID already exists. Return the bookings dictionary.

### 2. Update Tickets
`update_tickets(booking_id, new_ticket_count)`

Update the ticket count for an existing booking. Raise `KeyError("Booking not found")` when the booking ID is missing. Return the bookings dictionary.

### 3. Get Booking Details
`get_booking_details(booking_id)`

Return the booking record. Raise `KeyError("Booking not found")` when the booking ID is missing.

### 4. Get Group Bookings
`get_group_bookings(minimum_tickets)`

Return booking IDs whose ticket count is greater than or equal to the supplied minimum.

## Source Note

This specification is derived directly from the GitHub solution used for this practice question. No external requirements are added.
