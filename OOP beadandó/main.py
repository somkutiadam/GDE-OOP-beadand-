from DomesticFlight import DomesticFlight
from ForeignFlight import ForeignFlight
from Airline import Airline
from TicketReservation import TicketReservation


class FlightManager:
    def __init__(self):
        self.airline = Airline("MALÉV")
        self.reservations = []

        self.airline.add_flight(DomesticFlight("HU123", "Budapest", 15000))
        self.airline.add_flight(ForeignFlight("HU456", "London", 50000))
        self.airline.add_flight(DomesticFlight("HU789", "Debrecen", 20000))

        self.reservations.append(TicketReservation(self.airline.flight_search("HU123"), "Kiss Péter"))
        self.reservations.append(TicketReservation(self.airline.flight_search("HU456"), "Nagy Anna"))
        self.reservations.append(TicketReservation(self.airline.flight_search("HU789"), "Szabó János"))
        self.reservations.append(TicketReservation(self.airline.flight_search("HU123"), "Kovács Eszter"))
        self.reservations.append(TicketReservation(self.airline.flight_search("HU456"), "Tóth Gábor"))
        self.reservations.append(TicketReservation(self.airline.flight_search("HU789"), "Horváth Zoltán"))

    def reserve_ticket(self, flight_number, passanger_name):
        flight = self.airline.flight_search(flight_number)
        if flight:
            reservation = TicketReservation(flight, passanger_name)
            self.reservations.append(reservation)
            print(f"Sikeres foglalás: {passanger_name} - {flight.flight_type()} - {flight.flight_number} - {flight.destination} - {flight.ticket_price} Ft")
        else:
            print("A járat nem található.")

    def cancel_ticket(self, flight_number, passanger_name):
        for reservation in self.reservations:
            if reservation.flight.flight_number == flight_number and reservation.passanger_name == passanger_name:
                self.reservations.remove(reservation)
                print(f"Sikeres lemondás: {passanger_name} - {flight_number}")
                return
        print("A foglalás nem található.")

    def list_reservations(self):
        if not self.reservations:
            print("Nincsenek foglalások.")
        else:
            print("Foglalások:")
            for reservation in self.reservations:
                print(f"{reservation.passanger_name} - {reservation.flight.flight_type()} - {reservation.flight.flight_number} - {reservation.flight.destination} - {reservation.flight.ticket_price} Ft")
       


    
manager = FlightManager()

while True:
    print("\n--- Repülőjegy foglalási Rendszer ---")
    print("1. Repülőjegy foglalás")
    print("2. Repülőjegy lemondás")
    print("3. Foglalások listázása")
    print("4. Kilépés")
    choice = input("Válasszon egy lehetőséget (1-4): ")
    if choice == "1":
        flight_number = input("Adja meg a járatszámot: ")
        passanger_name = input("Adja meg az utas nevét: ")
        manager.reserve_ticket(flight_number, passanger_name)
    elif choice == "2":
        flight_number = input("Adja meg a járatszámot: ")
        passanger_name = input("Adja meg az utas nevét: ")
        manager.cancel_ticket(flight_number, passanger_name)
    elif choice == "3":     
        manager.list_reservations()
    elif choice == "4":
        break
    else:
        print("Érvénytelen választás. Kérjük, válasszon egy lehetőséget (1-4).")