class Car:
    def __init__(self, plate_number, brand, model, rate_per_day, availability):
        self.plate_number = plate_number
        self.brand = brand
        self.model = model
        self.rate_per_day = rate_per_day
        self.availability = availability

    def display_details(self):
        print(f"Plate Number: {self.plate_number} | Brand: {self.brand.value} | Model: {self.model}"
              f" | Rate: ₱{self.rate_per_day} | Availability: {'Available' if self.availability else 'Rented'}")

    def to_file_format(self):
        return f"{self.plate_number},{self.brand.value},{self.model},{self.rate_per_day},{self.availability}\n"

    def is_available(self):
        return self.availability