class MovieBookingSystem:
    def __init__(self):
        self.bookings = {}
    
    def create_booking(self, booking_id, customer_name, movie_name, tickets):
        if booking_id in self.bookings:
            raise ValueError("Booking already exists")
        self.bookings[booking_id] = {"customer_name": customer_name, "movie_name": movie_name, "tickets": tickets, "status": "Booked"}
        return self.bookings
    
    def update_tickets(self, booking_id, new_ticket_count):
        if booking_id not in self.bookings:
            raise KeyError("Booking not found")
        self.bookings[booking_id]["tickets"] = new_ticket_count
        return self.bookings
    
    def get_booking_details(self, booking_id):
        if booking_id not in self.bookings:
            raise KeyError("Booking not found")
        return self.bookings[booking_id]
    
    def get_group_bookings(self, minimum_tickets):
        group_bookings = []
        for key, val in self.bookings.items():
            if val["tickets"] >= minimum_tickets:
                group_bookings.append(key)
        return group_bookings
