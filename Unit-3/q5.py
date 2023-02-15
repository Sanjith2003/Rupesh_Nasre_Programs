class Room:
    def __init__(self, number, capacity, price):
        self.number = number
        self.capacity = capacity
        self.price = price
        self.is_booked = False

    def get_info(self):
        return f"Room {self.number}, capacity {self.capacity}, price ${self.price}/night"

    def book(self):
        if self.is_booked:
            raise ValueError(f"Room {self.number} is already booked")
        self.is_booked = True

    def cancel(self):
        self.is_booked = False

from hotel_reservation.rooms.room import Room
from hotel_reservation.rooms.suite import Suite
from hotel_reservation.rooms.deluxe import Deluxe
from hotel_reservation.guests.guest import Guest
from hotel_reservation.reservations.reservation import Reservation

# Create some sample rooms
rooms = [
    Room(101, 2, 100),
    Room(102, 2, 100),
    Suite(201, 4, 200),
    Deluxe(301, 2, 150),
]

# Create a list of guests
guests = [
    Guest("Alice", "Smith", "alice@example.com"),
    Guest("Bob", "Jones", "bob@example.com"),
    Guest("Charlie", "Brown", "charlie@example.com"),
]

# Create an empty list of reservations
reservations = []

# Define the main user interface
def main():
    while True:
        print("1. View available rooms")
        print("2. Make a reservation")
        print("3. View reservations")
        print("4. Cancel a reservation")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_available_rooms()
        elif choice == "2":
            make_reservation()
        elif choice == "3":
            view_reservations()
        elif choice == "4":
            cancel_reservation()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

def view_available_rooms():
    for room in rooms:
        if not room.is_booked:
            print(room.get_info())

def make_reservation():
    guest = select_guest()
    room = select_room()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    reservation = Reservation(guest, room, start_date, end_date)
    reservation.book()
    reservations.append(reservation)
    print("Reservation made:")
    print(reservation)

def select_guest():
    while True:
        print("Guests:")
        for i, guest in enumerate(guests):
            print(f"{i+1}. {guest}")
        choice = input("Select a guest (or enter a new guest name): ")
        if choice.isdigit():
            index = int(choice) - 1
            if index >= 0 and index < len(guests):
                return guests[index]
            else:
                print("Invalid choice")
        elif choice:
            first_name, last_name = choice.split()
            email = input("Enter email address: ")
            guest = Guest(first_name, last_name, email)
            guests.append(guest)
            return guest
        else:
            print("Invalid choice")

def select_room():
    while True:
        print("Rooms:")
        for i, room in enumerate(rooms):
            if not room.is_booked:
                print(f"{i+1}. {room.get_info()}")
        choice = input("Select a room: ")
        if choice.isdigit():
            index = int(choice) - 1
            if index >= 0 and index < len(rooms):
                room = rooms[index]
                if not room.is_booked:
                    return room
                else:
                    print("That room is already booked")
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")

def view_reservations():
    for reservation in reservations:
        print(reservation)

def cancel_reservation():
    while True:
        print("Reservations:")
        for i, reservation in enumerate(reservations):
            print(f"{i+1}. {reservation}")
        choice = input("Select a reservation to cancel: ")
        if choice.isdigit():
            index = int(choice) - 1
            if index >= 0 and index < len(reservations):
                reservation = reservations[index]
                reservation.cancel()
                reservations.pop(index)
                print("Reservation cancelled")
                break
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()



