from utils.Enums import RentalStatus


class Rental:

    def __init__(self, rental_id, customer_id, car_plate, days, total_cost, status, rental_date):
        self.rental_id = rental_id
        self.customer_id = customer_id
        self.car_plate = car_plate
        self.days = days
        self.total_cost = total_cost
        self.status = status
        self.rental_date = rental_date

    def display_rental_details(self):
        print("Rental Details:")
        print(f"Rental ID: {self.rental_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Car Plate: {self.car_plate}")
        print(f"Days: {self.days}")
        print(f"Total Cost: {self.total_cost}")
        print(f"Status: {self.status.value}")
        print(f"Rental Date: {self.rental_date}")

    def calculate_total_cost(self, rate_per_day):
        self.total_cost = self.days * rate_per_day

    def mark_returned(self):
        self.status = RentalStatus.RETURNED

    def is_ongoing(self):
        return self.status == RentalStatus.ONGOING

    def to_file_format(self):
        return f"{self.rental_id},{self.customer_id},{self.car_plate},{self.days},{self.total_cost},{self.status.value},{self.rental_date}\n"