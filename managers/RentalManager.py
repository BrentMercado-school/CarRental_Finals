import os
from tabulate import tabulate

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
        print("\n" + "=" * 45)
        print("             RENT A CAR")
        print("=" * 45)

        customer_id = get_valid_integer(
            "Enter customer ID",
            "Please enter a valid whole number."
        )
        customer = self.customer_manager.get_customer_by_id(customer_id)

        if not customer:
            print("\nCustomer not found.")
            return

        print(f"\nSelected Customer: {customer.name} (ID: {customer.customer_id})")

        print("\nAvailable Cars:")
        available_cars = [car for car in self.car_manager.cars if car.is_available()]
        if not available_cars:
            print("[INFO] No cars available for rent.")
            return

        car_data = []
        for car in available_cars:
            car_data.append({
                "Plate Number": car.plate_number,
                "Brand": car.brand.value,
                "Model": car.model,
                "Rate / Day (₱)": car.rate_per_day,
                "Availability": "Available" if car.availability else "Rented"
            })

        print(tabulate(car_data, headers="keys", tablefmt="pipe"))

        car_plate_to_rent = input("\nEnter car plate to rent: ").strip().upper()
        car_to_rent = self.car_manager.get_car_by_plate_number(car_plate_to_rent)

        if not car_to_rent:
            print("\nCar not found.")
            return

        if not car_to_rent.is_available():
            print("\nCar is already rented.")
            return

        days = get_valid_integer(
            "Enter number of rental days",
            "Please enter a valid whole number."
        )

        if days <= 0:
            print("\nNumber of days must be greater than 0.")
            return

        rental = Rental(
            rental_id=self.next_rental_id,
            customer_id=customer.customer_id,
            car_plate=car_to_rent.plate_number,
            days=days,
            total_cost=0,
            status=RentalStatus.ONGOING,
            rental_date=create_date_format()
        )

        rental.calculate_total_cost(car_to_rent.rate_per_day)

        self.rentals.append(rental)
        customer.rented_cars.append(car_to_rent.plate_number)
        self.next_rental_id += 1
        car_to_rent.availability = False

        print("\n" + "=" * 45)
        print(f"Rental created successfully! Rental ID: {rental.rental_id}")
        print(f"Customer      : {customer.name} (ID: {customer.customer_id})")
        print(f"Car Plate     : {car_to_rent.plate_number} ({car_to_rent.brand.value} {car_to_rent.model})")
        print(f"Rental Days   : {days}")
        print(f"Total Cost    : ₱{rental.total_cost}")
        print("=" * 45)

        input("Press Enter to continue...")

    def get_rental_by_id(self, rental_id):
        for rental in self.rentals:
            if rental.rental_id == rental_id:
                return rental
        return None

    def return_car(self):
        print("\n" + "=" * 45)
        print("            RETURN CAR")
        print("=" * 45)

        rental_id = get_valid_integer(
            "Enter rental ID to return",
            "Please enter a valid whole number."
        )

        rental = self.get_rental_by_id(rental_id)

        if not rental:
            print("\nRental not found.")
            return

        if rental.status == RentalStatus.RETURNED:
            print("\nCar has already been returned.")
            return

        rental_data = [{
            "Rental ID": rental.rental_id,
            "Customer ID": rental.customer_id,
            "Car Plate": rental.car_plate,
            "Days": rental.days,
            "Total Cost (₱)": rental.total_cost,
            "Status": rental.status.value,
            "Rental Date": rental.rental_date
        }]

        print("\nRental Details:")
        print(tabulate(rental_data, headers="keys", tablefmt="pipe"))

        while True:
            choice = input("\nDo you want to return this car? (Y/N): ").strip().upper()
            if choice == "Y":
                car = self.car_manager.get_car_by_plate_number(rental.car_plate)
                if car:
                    car.availability = True

                customer = self.customer_manager.get_customer_by_id(rental.customer_id)
                if customer and rental.car_plate in customer.rented_cars:
                    customer.rented_cars.remove(rental.car_plate)

                rental.mark_returned()

                print("\n" + "=" * 45)
                print(f"Car {rental.car_plate} returned successfully!")
                print(f"Rental ID    : {rental.rental_id}")
                print(f"Customer ID  : {rental.customer_id}")
                print(f"Total Paid   : ₱{rental.total_cost}")
                print("=" * 45)
                input("Press Enter to continue...")
                return

            elif choice == "N":
                print("\nCar return canceled.")
                return

            else:
                print("Please enter Y or N.")

    def display_rentals(self):
        if len(self.rentals) == 0:
            print("\nNo rentals available.")
            return

        data = []
        for rental in self.rentals:
            data.append({
                "Rental ID": rental.rental_id,
                "Customer ID": rental.customer_id,
                "Car Plate": rental.car_plate,
                "Days": rental.days,
                "Total Cost (₱)": rental.total_cost,
                "Status": rental.status.value,
                "Rental Date": rental.rental_date
            })

        print("RENTAL LIST")
        print(tabulate(data, headers="keys", tablefmt="pipe"))

        input("Press Enter to continue...")

    def display_rentals_by_customer(self):
        print("\n" + "=" * 50)
        print("       CUSTOMER RENTED CARS")
        print("=" * 50)

        customer_id = get_valid_integer(
            "Enter customer ID",
            "Please enter a valid whole number."
        )

        customer = self.customer_manager.get_customer_by_id(customer_id)

        if not customer:
            print("\nCustomer not found.")
            return

        if not customer.rented_cars:
            print(f"\nCustomer '{customer.name}' has no rented cars.")
            return

        data = []
        for plate in customer.rented_cars:
            car = self.car_manager.get_car_by_plate_number(plate)
            if car:
                data.append({
                    "Plate Number": car.plate_number,
                    "Brand": car.brand.value,
                    "Model": car.model,
                    "Rate / Day (₱)": car.rate_per_day,
                    "Availability": "Available" if car.availability else "Rented"
                })

        print(f"\nRented Cars for Customer: {customer.name} (ID: {customer.customer_id})\n")
        print(tabulate(data, headers="keys", tablefmt="pipe"))

        input("\nPress Enter to continue...")

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
        returned_rentals = [r for r in self.rentals if r.status == RentalStatus.RETURNED]

        if not returned_rentals:
            print("\nNo returned cars found.")
            return

        data = []
        for rental in returned_rentals:
            car = self.car_manager.get_car_by_plate_number(rental.car_plate)
            customer = self.customer_manager.get_customer_by_id(rental.customer_id)

            if car and customer:
                data.append({
                    "Rental ID": rental.rental_id,
                    "Plate Number": rental.car_plate,
                    "Brand": car.brand.value,
                    "Model": car.model,
                    "Total Cost (₱)": rental.total_cost,
                    "Customer Name": customer.name,
                    "Status": rental.status.value,
                    "Rental Date": rental.rental_date
                })

        print(f"\nTOTAL RETURNED CARS ({len(returned_rentals)})")

        print(tabulate(data, headers="keys", tablefmt="pipe"))

        input("\nPress Enter to continue...")

    def save_file(self, rental_filename, customer_manager, customer_filename, car_manager, car_filename):
        with open(rental_filename, "w") as file:
            for rental in self.rentals:
                file.write(rental.to_file_format())

        customer_manager.save_file_rented(customer_filename)
        car_manager.save_file_rented(car_filename)

        print(f"Saved {len(self.rentals)} rental(s) to {rental_filename}.")

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