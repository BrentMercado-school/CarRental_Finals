import os.path
from utils.Enums import *
from utils.Helper import *
from classes.Car import Car
from tabulate import tabulate

class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        print("\n" + "=" * 29)
        print("        ADD NEW CAR")
        print("=" * 29)

        plate_number = generate_plate_number()
        print(f"\nPlate Number Generated: {plate_number}")

        print("\n1. Select Car Brand")
        print("-" * 25)
        for brand in CarBrand:
            print(f"• {brand.value}")

        brand_input = get_non_empty_input(
            "\nEnter car brand",
            "Car brand should not be empty."
        )

        car_brand = get_car_brand_from_input(brand_input)

        if car_brand is None:
            print("\n[ERROR] Invalid brand selected. Car not added.")
            return

        print("\n2. Select Car Model")
        print("-" * 25)
        print(f"Available models for {car_brand.value}:")
        for model in BRAND_MODELS[car_brand]:
            print(f"• {model}")

        model_input = get_non_empty_input(
            "\nEnter car model",
            "Car model should not be blank."
        ).title()

        if model_input not in BRAND_MODELS[car_brand]:
            print("\n[ERROR] Invalid model for the selected brand.")
            return

        print("\n3. Set Rental Rate")
        print("-" * 25)
        car_rate = get_valid_integer(
            "Enter car rate per day",
            "Invalid input. Please enter a valid number."
        )

        availability = True
        self.cars.append(Car(
            plate_number,
            car_brand,
            model_input,
            car_rate,
            availability
        ))

        print("\n" + "=" * 35)
        print("Car added successfully!")
        print(f"Plate Number : {plate_number}")
        print(f"Brand        : {car_brand.value}")
        print(f"Model        : {model_input}")
        print(f"Rate / Day   : {car_rate}")
        print("Status       : Available")
        print("=" * 35)
        input("Press Enter to continue...")

    def get_car_by_plate_number(self, plate_number):
        for car in self.cars:
            if car.plate_number == plate_number:
                return car
        return None

    def remove_car(self):
        print("\n" + "=" * 45)
        print("        REMOVE CAR")
        print("=" * 45)

        plate_number = get_non_empty_input(
            "Enter plate number of car to remove",
            "Plate number cannot be empty."
        ).upper()

        car = self.get_car_by_plate_number(plate_number)

        if car is None:
            print("\nCar not found.")
            return

        print("\nCAR DETAILS")
        print("-" * 90)
        car.display_details()

        confirm = input(
            f"\nAre you sure you want to remove this car? (Y/N): "
        ).strip().upper()

        if confirm != "Y":
            print("\nCar removal canceled.")
            return

        self.cars.remove(car)

        print("\n" + "=" * 45)
        print(f"Car {plate_number} removed successfully.")
        print("=" * 45)

    def display_cars(self):
        if len(self.cars) == 0:
            print("Car list is empty.")
            return

        data = []

        for car in self.cars:
            data.append({
                "Plate Number": car.plate_number,
                "Brand": car.brand.value,
                "Model": car.model,
                "Rate / Day (₱)": car.rate_per_day,
                "Availability": "Available" if car.availability else "Rented"
            })

        table = tabulate(data, headers="keys", tablefmt="pipe")
        print("\nCAR LIST")
        print(table)

        input("\nPress Enter to continue...")

    def add_test_car(self):
        self.cars.append(Car("a", CarBrand.TOYOTA, "Vios", 1500, True))
        self.cars.append(Car("aa", CarBrand.TOYOTA, "Vios", 1500, True))
        self.cars.append(Car("BBB 222", CarBrand.HONDA, "Civic", 1800, True))
        self.cars.append(Car("CCC 333", CarBrand.MITSUBISHI, "Xpander", 2000, False))
        self.cars.append(Car("DDD 444", CarBrand.NISSAN, "Terra", 2500, True))

    def update_car(self):
        print("\n" + "=" * 45)
        print("        UPDATE CAR DETAILS")
        print("=" * 45)

        plate_number = get_non_empty_input(
            "Enter plate number of car to update",
            "Plate number cannot be empty."
        ).upper()

        founded_car = self.get_car_by_plate_number(plate_number)

        if founded_car is None:
            print("\n Car not found.")
            return

        print("\nCURRENT CAR DETAILS")
        print("-" * 45)
        founded_car.display_details()

        print("\nPress ENTER to keep the current value.")

        print("\n1. Update Car Brand")
        print("-" * 25)
        for brand in CarBrand:
            print(f"• {brand.value}")

        brand_input = input(
            f"\nEnter new car brand (current: {founded_car.brand.value}): "
        ).strip()

        if brand_input == "":
            new_brand = founded_car.brand
        else:
            new_brand = get_car_brand_from_input(brand_input)
            if new_brand is None:
                print("\nInvalid brand. Update canceled.")
                return

        print("\n2. Update Car Model")
        print("-" * 25)
        print(f"Available models for {new_brand.value}:")
        for model in BRAND_MODELS[new_brand]:
            print(f"• {model}")

        model_input = input(
            f"\nEnter new car model (current: {founded_car.model}): "
        ).strip().title()

        if model_input == "":
            new_model = founded_car.model
        elif model_input in BRAND_MODELS[new_brand]:
            new_model = model_input
        else:
            print("\nInvalid model for selected brand.")
            return

        print("\n3. Update Rental Rate")
        print("-" * 25)
        rate_input = input(
            f"Enter new rate per day (current: ₱{founded_car.rate_per_day}): "
        ).strip()

        if rate_input == "":
            new_rate = founded_car.rate_per_day
        else:
            try:
                new_rate = int(rate_input)
            except ValueError:
                print("\nInvalid rate. Update canceled.")
                return

        founded_car.brand = new_brand
        founded_car.model = new_model
        founded_car.rate_per_day = new_rate

        print("\n" + "=" * 90)
        print("Car details updated successfully!")
        print("-" * 90)
        founded_car.display_details()
        print("=" * 90)

        input("Press Enter to continue...")

    def search_by_brand(self):
        print("\n" + "=" * 45)
        print("        SEARCH CARS BY BRAND")
        print("=" * 45)

        print("\nAvailable Brands:")
        print("-" * 25)
        for brand in CarBrand:
            print(f"• {brand.value}")

        brand_input = input("\nEnter car brand to search: ").strip()
        selected_brand = get_car_brand_from_input(brand_input)

        if selected_brand is None:
            print(f"\nBrand '{brand_input}' not found.")
            return

        filtered_cars = [car for car in self.cars if car.brand == selected_brand]

        if not filtered_cars:
            print(f"\nNo cars available under brand {selected_brand.value}.")
            return

        data = []
        for car in filtered_cars:
            data.append({
                "Plate Number": car.plate_number,
                "Brand": car.brand.value,
                "Model": car.model,
                "Rate / Day (₱)": car.rate_per_day,
                "Availability": "Available" if car.availability else "Rented"
            })

        print("\n" + "=" * 45)
        print(f"{len(filtered_cars)} car(s) found under {selected_brand.value}")
        print("=" * 45)

        table = tabulate(data, headers="keys", tablefmt="pipe")
        print(table)

        input("Press Enter to continue...")

    def search_by_model(self):
        print("\n" + "=" * 45)
        print("        SEARCH CARS BY MODEL")
        print("=" * 45)

        model_input = input("\nEnter car model to search: ").strip().title()

        valid_models = set()
        for models in BRAND_MODELS.values():
            valid_models.update(models)

        if model_input not in valid_models:
            print(f"\nModel '{model_input}' does not exist.")
            return

        filtered_cars = [car for car in self.cars if car.model == model_input]

        if not filtered_cars:
            print(f"\nNo cars available under model {model_input}.")
            return

        data = []
        for car in filtered_cars:
            data.append({
                "Plate Number": car.plate_number,
                "Brand": car.brand.value,
                "Model": car.model,
                "Rate / Day (₱)": car.rate_per_day,
                "Availability": "Available" if car.availability else "Rented"
            })

        print("\n" + "=" * 45)
        print(f"{len(filtered_cars)} car(s) found under model {model_input}")
        print("=" * 45)
        print(tabulate(data, headers="keys", tablefmt="pipe"))

        input("Press Enter to continue...")

    def search_by_availability(self):
        print("\n" + "=" * 45)
        print("        SEARCH CARS BY AVAILABILITY")
        print("=" * 45)

        available_cars = [car for car in self.cars if car.is_available()]
        unavailable_cars = [car for car in self.cars if not car.is_available()]

        print("\nAVAILABLE CARS")
        print("-" * 45)

        if not available_cars:
            print("No available cars.")
        else:
            available_data = []
            for car in available_cars:
                available_data.append({
                    "Plate Number": car.plate_number,
                    "Brand": car.brand.value,
                    "Model": car.model,
                    "Rate / Day (₱)": car.rate_per_day,
                    "Status": "Available"
                })

            print(tabulate(available_data, headers="keys", tablefmt="pipe"))

        print("\nUNAVAILABLE (RENTED) CARS")
        print("-" * 45)

        if not unavailable_cars:
            print("No rented cars.")
        else:
            unavailable_data = []
            for car in unavailable_cars:
                unavailable_data.append({
                    "Plate Number": car.plate_number,
                    "Brand": car.brand.value,
                    "Model": car.model,
                    "Rate / Day (₱)": car.rate_per_day,
                    "Status": "Rented"
                })

            print(tabulate(unavailable_data, headers="keys", tablefmt="pipe"))

            input("Press Enter to continue...")

    def save_file(self, filename):
        with open(filename, "w") as file:
            for car in self.cars:
                file.write(car.to_file_format())

        print(f"Saved {len(self.cars)} car(s) to {filename}.")

    def load_file(self, filename):

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
                if len(parts) == 5:
                    plate_number = parts[0]
                    brand_str = parts[1]
                    model = parts[2]
                    rate_per_day = int(parts[3])
                    availability = parts[4] == "True"

                    try:
                        brand = CarBrand[brand_str.upper()]
                    except KeyError:
                        print(f"Unknown brand '{brand_str}' in file. Skipping this car.")
                        continue

                    self.cars.append(Car(plate_number, brand, model, rate_per_day, availability))

        print(f"Loaded {len(self.cars)} car(s) from {filename}\n")

