from Flight import Flight

class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, ticket_price):
        super().__init__(flight_number, destination, ticket_price)

    def flight_type(self):
        return "Belföldi járat"
    