# User and admin login:
def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == "user" and password == "user123":
            print("Login successful! Welcome, user.")
            return "user"
        elif username == "admin" and password == "admin123":
            print("Login successful! Welcome, admin.")
            return "admin"
        else:
            print("Error! Wrong username or password. Please try again.")

# User Functions:
#1
def user_menu():
    print("Welcome, User:")
    print("1. Book a ticket")
    print("2. Cancel a booking")
    print("3. Show flights")
    choice = input("Enter the corresponding number: ")
    return choice

#2
def select_flight(flights):
    print("Available Flights:")
    for index, flight in enumerate(flights):
        print(f"{index+1}. {flight}")
    choice = int(input("Choose a flight (enter the corresponding number): "))
    return flights[choice-1]

#3
def display_seat_availability(flight, seat_layout):
    print(f"{flight} - Seat Layout:")
    for row, seats in enumerate(seat_layout):
        print(f"Row {row+1}: ", end="")
        for seat in seats:
            if seat == "*":
                print("* ", end="")
            else:
                print("X ", end="")
        print()
    row_number = int(input("Enter the row number: "))
    seat_number = input("Enter the seat number: ")
    return row_number, seat_number

#4
def book_seat(flight, seat_layout, row_number, seat_number):
    if seat_layout[row_number-1][seat_number] == "*":
        seat_layout[row_number-1][seat_number] = "X"
        print(f"Seat {seat_number} in Row {row_number} has been successfully booked!")
    else:
        print("Error! The seat is already booked.")

#5
def store_booking_confirmation(name, flight, row_number, seat_number):
    ticket = f"Name: {name}\nFlight: {flight}\nTicket: Row {row_number} Seat {seat_number}\n"
    with open("booking.txt", "a") as file:
        file.write(ticket)
    print("Booking confirmation has been stored.")

#6
def cancel_booking(flight, seat_layout, row_number, seat_number):
    if seat_layout[row_number-1][seat_number] == "X":
        seat_layout[row_number-1][seat_number] = "*"
        print(f"Booking for seat {seat_number} in Row {row_number} has been cancelled.")
    else:
        print("Error! The seat is not booked.")
        
        
#7
def show_flights(flights, seat_layouts):
    for index, flight in enumerate(flights):
        print(f"Flight: {flight}")
        print(f"Seat Layout: {seat_layouts[index]}")
        print()



# Admin Functions:
#1
def admin_menu():
    print("Welcome Admin:")
    print("1. Add a flight")
    print("2. Modify a flight")
    print("3. Remove a flight")
    choice = input("Enter the corresponding number: ")
    return choice
#2
def manage_flight_details(flights, seat_layouts):
    print("Enter Flight Company to Manage:")
    print("1. Flight Company A")
    print("2. Flight Company B")
    company_choice = input("Enter the corresponding number: ")

    if company_choice == "1":
        modify_flight_details(flights[0], seat_layouts[0])
    elif company_choice == "2":
        modify_flight_details(flights[1], seat_layouts[1])
    else:
        print("Invalid choice")
#3
def modify_flight_details(flight, seat_layout):
    print("What changes do you want to make?")
    print("1. Change arrival and departure time")
    print("2. Change flight details")
    print("3. Change the seat layout")
    change_choice = input("Enter the corresponding number: ")

    if change_choice == "1":
        # Logic to change arrival and departure time
        pass
    elif change_choice == "2":
        # Logic to change flight details
        pass
    elif change_choice == "3":
        # Logic to change the seat layout
        pass
    else:
        print("Invalid choice")

# Example usage
def main():
    role = login()
    print("Role:", role)

    if role == "user":
        user_choice = user_menu()
        if user_choice == "1":
            flight = select_flight(flights)
            row, seat = display_seat_availability(flight, seat_layouts[flights.index(flight)])
            book_seat(flight, seat_layouts[flights.index(flight)], row, seat)
            store_booking_confirmation("Hamza", flight, row, seat)
        elif user_choice == "2":
            flight = select_flight(flights)
            row, seat = display_seat_availability(flight, seat_layouts[flights.index(flight)])
            cancel_booking(flight, seat_layouts[flights.index(flight)], row, seat)
        elif user_choice == "3":
            show_flights(flights, seat_layouts)
        else:
            print("Invalid choice.")

    elif role == "admin":
        admin_choice = admin_menu()
        if admin_choice == "2":
            manage_flight_details(flights, seat_layouts)
        else:
            print("Invalid choice.")

# Example data
flights = ["Flight Company A", "Flight Company B"]
seat_layouts = [
    [["*", "*", "*", "*", "*"], ["*", "*", "X", "*", "*"], ["X", "X", "*", "*", "X"]],
    [["*", "X", "X", "*", "*"], ["*", "*", "*", "*", "*"], ["X", "X", "X", "*", "X"]]
]

main()