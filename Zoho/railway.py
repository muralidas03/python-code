class Train:
    def _init_(self, train_number, name, seats_available):
        self.train_number = '12345'
        self.name = 'Express 123'
        self.seats_available = 100

class Passenger:
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Reservation:
    def _init_(self, train, passenger):
        self.train = train
        self.passenger = passenger
        self.confirmation_number = self.generate_confirmation_number()

    def generate_confirmation_number(self):
        # Generate a unique confirmation number based on some logic
        pass

    def make_reservation(self):
        if self.train.seats_available > 0:
            self.train.seats_available -= 1
            print(f"Reservation successful! Confirmation number: {self.confirmation_number}")
        else:
            print("Sorry, no seats available on this train.")

# Example usage
train1 = Train()
passenger1 = Passenger("John Doe", 30, "Male")
reservation1 = Reservation(train1, passenger1)
reservation1.make_reservation()