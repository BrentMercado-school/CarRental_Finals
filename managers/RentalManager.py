import os

from classes.Rental import Rental
from utils.Enums import RentalStatus
from utils.Helper import get_valid_integer, create_date_format


class RentalManagement:
    def __init__(self, customer_manager, car_manager):
        self.rentals = []
        self.next_rental_id = 1
        self.customer_manager = customer_manager
        self.car_manager = car_manager

    def rent_car(self):
        customer_id = get_valid_integer("Enter customer ID", "Enter a valid whole number")
        customer = self.customer_manager.get_customer_by_id(customer_id)

        if not customer:
            print("Customer not found")
            return

        self.car_manager.display_cars()
        car_plate_to_rent = input("\nEnter car plate to rent: ").strip().upper()
        car_to_rent = self.car_manager.get_car_by_plate_number(car_plate_to_rent)

        if not car_to_rent:
            print("Car not found")
            return

        if not car_to_rent.is_available:
            print("Car is already rented")
            return

        days = get_valid_integer("Enter days", "Enter a valid whole number")

        if days <= 0:
            print("Invalid days")
            return

        rental = Rental(
            rental_id = self.next_rental_id,
            customer_id = customer.customer_id,
            car_plate = car_plate_to_rent,
            days = days,
            total_cost = 0,
            status = RentalStatus.ONGOING,
            rental_date = create_date_format()
        )

        rental.calculate_total_cost(car_to_rent.rate_per_day)

        self.rentals.append(rental)
        customer.rented_cars.append(car_to_rent.plate_number)
        self.next_rental_id += 1
        car_to_rent.is_available = False
        print(f"Rental created! Rental ID: {rental.rental_id}")

    def get_rental_by_id(self, rental_id):
        for rental in self.rentals:
            if rental.rental_id == rental_id:
                return rental
        return None

    def return_car(self):
        rental_id = get_valid_integer("Enter rental ID", "Enter a valid whole number")
        rental = self.get_rental_by_id(rental_id)

        if not rental:
            print("Rental not found")
            return

        if not rental.ongoing():
            print("Car already returned")
            return

        rental.display_rental_details()

        while True:
            choice = input("Do you want to return this car? (Y/N): ").strip().lower()

            if choice == "y":
                car = self.car_manager.get_car_by_plate_number(rental.car_plate)
                if car:
                    car.is_available = True

                customer = self.customer_manager.get_customer_by_id(rental.customer_id)
                if customer and rental.car_plate in customer.rented_cars:
                    customer.rented_cars.remove(rental.car_plate)

                rental.mark_returned()

                print(f"Car {rental.car_plate} returned successfully.")
                return

            elif choice == "n":
                print("Car not returned")
                return

            else:
                print("Please enter Y or N")
                continue

    def display_rentals(self):
        for rent in self.rentals:
            rent.display_rental_details()

    def display_rentals_by_customer(self):
        customer_id = get_valid_integer("Enter customer ID", "Enter a valid whole number")
        customer = self.customer_manager.get_customer_by_id(customer_id)

        if not customer:
            print("Customer not found")
            return

        for plate in customer.rented_cars:
            car = self.car_manager.get_car_by_plate_number(plate)
            if car:
                car.display_details()

    def search_by_rented_cars(self):
        rented_info = []
        for car in self.car_manager.cars:
            if not car.is_available:

                rental = next(
                    (r for r in self.rentals if r.car_plate == car.plate_number and r.status == RentalStatus.ONGOING),
                    None
                )
                if rental:
                    customer = self.customer_manager.get_customer_by_id(rental.customer_id)
                    rented_info.append((car, customer))

        for car, customer in rented_info:
            print(f"Car: {car.plate_number} ({car.brand.name} {car.model})")
            print(f"Rented by: {customer.name if customer else 'Unknown'}")
            print("-" * 20)

    def search_by_returned_cars(self):
        returned_info = []

        for rental in self.rentals:
            if rental.status == RentalStatus.RETURNED:
                returned_info.append(rental)

        if not returned_info:
            print("No returned cars found.")
            return

        print("=" * 90)
        print("Rental ID | Plate No | Brand | Model | Total Cost | Customer Name | Status | Rental Date")
        print("-" * 90)

        for rental in returned_info:
            car = self.car_manager.get_car_by_plate_number(rental.car_plate)
            customer = self.customer_manager.get_customer_by_id(rental.customer_id)

            if car and customer:
                print(
                    f"{rental.rental_id:<9} | "
                    f"{rental.car_plate:<8} | "
                    f"{car.brand.value:<5} | "
                    f"{car.model:<10} | "
                    f"{rental.total_cost:<10} | "
                    f"{customer.name:<13} | "
                    f"{rental.status.name:<8} | "
                    f"{rental.rental_date}"
                )

        print("-" * 90)
        print(f"Total returned cars: {len(returned_info)}")
        print("=" * 90)

    def save_file(self, filename):
        with open(filename, "w") as file:
            for rental in self.rentals:
                file.write(rental.to_file_format())

            print(f"Saved {len(self.rentals)} rental(s) to {filename}.")

    def load_file(self, filename):
        self.rentals = []

        if not os.path.exists(filename):
            print(f"No existing {filename} found. Starting with an empty list.\n")
            return

        with open(filename, "r") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")

                if len(parts) == 7:
                    rental_id = int(parts[0])
                    customer_id = int(parts[1])
                    car_plate = parts[2]
                    days = int(parts[3])
                    total_cost = float(parts[4])
                    status = RentalStatus(parts[5])
                    rental_date = parts[6]

                    self.rentals.append(Rental(rental_id, customer_id, car_plate, days, total_cost, status, rental_date))

            if self.rentals:
                self.next_rental_id = max(r.rental_id for r in self.rentals) + 1

            print(f"Loaded {len(self.rentals)} rental(s) from {filename}\n")