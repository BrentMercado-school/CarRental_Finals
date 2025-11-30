class Car:
    def __init__(self, plate_number, brand, model, rate_per_day, availability):
        self.plate_number = plate_number
        self.brand = brand
        self.model = model
        self.rate_per_day = rate_per_day
        self.availability = availability

    def display_car_details(self):
        print(f"Plate Number: {self.plate_number} | Brand: {self.brand} | Model: {self.model}"
              f"Rate: {self.rate_per_day} | Availability: {self.availability}")

    def is_available(self):
        pass