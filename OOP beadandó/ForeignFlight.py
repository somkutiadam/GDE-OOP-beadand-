from Flight import Flight

class ForeignFlight(Flight):
    def __init__(self, flight_number, destination, ticket_price):
        super().__init__(flight_number, destination, ticket_price)

    def flight_type(self):
        return "Külföldi járat"