class Train:
    def __init__(self, train_no, name, seats):
        self.train_no = train_no
        self.name = name
        self.seats = seats
        self.passengers = []

    def book_ticket(self, name):
        if len(self.passengers) < self.seats:
            self.passengers.append(name)
            print(f"Ticket booked for {name} on train {self.name}.")
            return True
        else:
            print("This train is full. Try another train.")
            return False

    def cancel_ticket(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
            print(f"Ticket cancelled for {name}.")
        else:
            print(f"No reservation found for {name}.")

    def view_reservations(self):
        print(f"Passengers on train {self.name}: {', '.join(self.passengers)}")


# Example usage:
train1 = Train(101, "Shatabdi Express", 2)
train1.book_ticket("Alice")
train1.book_ticket("Bob")
train1.view_reservations()
train1.cancel_ticket("Alice")
train1.view_reservations()
