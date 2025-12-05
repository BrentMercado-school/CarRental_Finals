import os.path
from utils.Enums import *
from utils.Helper import *
from classes.Car import Car

class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        plate_number = generate_plate_number()
        print(f"Automatically generated plate number: {plate_number}")

        print(f"\nAvailable Brands:")
        for brand in CarBrand:
            print(f"- {brand.value}")

        brand_input = get_non_empty_input(
            "Enter car brand",
            "Car brand should not be empty."
        ).upper()

        try:
            car_brand = CarBrand[brand_input]
        except KeyError:
            print("Invalid brand. Car not added.")
            return

        print(f"\nAvailable Models for {car_brand.value}:")
        for model in BRAND_MODELS[car_brand]:
            print(f"- {model}")

        model_input = get_non_empty_input(
            "Enter car model",
            "Car model should not be blank."
        ).title()

        if model_input not in BRAND_MODELS[car_brand]:
            print("Invalid model for selected brand!")
            return

        car_model = model_input

        car_rate = get_valid_integer("Enter car rate", "Invalid input. Try again.")

        availability = True

        self.cars.append(Car(plate_number, car_brand, car_model, car_rate, availability))
        print(f"Successfully added car {plate_number} to car management.")

    def get_car_by_plate_number(self, plate_number):
        for car in self.cars:
            if car.plate_number == plate_number:
                return car
        return None

    def remove_car(self):
        plate_number = get_non_empty_input("Enter plate number", "Input cannot be empty.")
        car = self.get_car_by_plate_number(plate_number)

        if car is None:
            print("Car not found.")
            return

        self.cars.remove(car)
        print(f"Successfully removed car {plate_number}.")

    def display_cars(self):
        if len(self.cars) == 0:
            print("Car list is empty.")
            return
        for car in self.cars:
            car.display_details()

    def add_test_car(self):
        self.cars.append(Car("a", CarBrand.TOYOTA, "Vios", 1500, True))
        self.cars.append(Car("aa", CarBrand.TOYOTA, "Vios", 1500, True))
        self.cars.append(Car("BBB 222", CarBrand.HONDA, "Civic", 1800, True))
        self.cars.append(Car("CCC 333", CarBrand.MITSUBISHI, "Xpander", 2000, False))
        self.cars.append(Car("DDD 444", CarBrand.NISSAN, "Terra", 2500, True))

    def update_car(self):
        plate_number = get_non_empty_input("Enter plate number", "Invalid input")
        founded_car = self.get_car_by_plate_number(plate_number)

        if founded_car is None:
            print("Car not found.")
            return

        founded_car.display_car_details()
        print(f"Press ENTER to keep current details of {founded_car.plate_number}.")

        for brand in CarBrand:
            print(f"- {brand.value}")

        brand_input = input(f"Enter new car brand (current: {founded_car.brand} ").strip().upper()

        if brand_input == "":
            new_brand = founded_car.brand
        else:
            try:
                new_brand = CarBrand[brand_input]
            except KeyError:
                print("Invalid brand. Car not added.")
                return

        print(f"\nAvailable Models for {new_brand.value}:")
        for brand in BRAND_MODELS[new_brand]:
            print(f"- {brand}")

        model_input = get_non_empty_input(
            "Enter new car model",
            "Car model should not be blank."
        ).strip().title()

        if model_input in BRAND_MODELS[new_brand]:
            new_model = model_input
        else:
            print("Invalid model for selected brand!")
            return

        new_rate_input = input("Enter new car rate: ").strip()

        if new_rate_input == "":
            new_rate = founded_car.rate_per_day
        else:
            try:
                new_rate = int(new_rate_input)
            except ValueError:
                print("Invalid rate. Update canceled.")
                return


        founded_car.brand = new_brand
        founded_car.model = new_model
        founded_car.rate_per_day = new_rate

        print("Successfully updated car details.")

    def search_by_brand(self):
        brand_input = input("Enter car brand: ").strip().upper()

        try:
            selected_brand = CarBrand[brand_input]
        except KeyError:
            print(f"No brand {brand_input} found")
            return

        filtered_cars = [car for car in self.cars if car.brand == selected_brand]
        if len(filtered_cars) == 0:
            print(f"No cars yet in brand {brand_input}.")
            return
        print(f"Found {len(filtered_cars)} car(s) in brand {brand_input}.")
        for car in filtered_cars:
            car.display_details()

    def search_by_model(self):
        model_input = input("Enter car model: ").strip().title()

        found = False
        for brand, models in BRAND_MODELS.items():
            if model_input in models:
                found = True
                break
        if not found:
            print(f"No cars yet in model {model_input}.")
            return

        filtered_cars = [car for car in self.cars if car.model == model_input]
        if len(filtered_cars) == 0:
            print(f"No cars yet in model {model_input}.")
            return
        print(f"Found {len(filtered_cars)} car(s) in model {model_input}.")
        for car in filtered_cars:
            car.display_details()

    def search_by_availability(self):
        available_cars = [car for car in self.cars if car.availability == True]
        unavailable_cars = [car for car in self.cars if car.availability == False]
        print("-- Available cars --")
        for car in available_cars:
            car.display_details()
        print("\n-- Unavailable cars --")
        for car in unavailable_cars:
            car.display_details()

    def save_file(self, filename):
        with open(filename, "w") as file:
            for car in self.cars:
                file.write(car.to_file_format())

        print(f"Saved {len(self.cars)} car(s) to {filename}.")

    def load_file(self, filename):
        if not os.path.exists(filename):
            print("No existing file found. Starting with an empty list.\n")
            return []

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
                    rate_per_day = parts[3]
                    availability = parts[4] == "True"

                    try:
                        brand = CarBrand[brand_str.upper()]
                    except KeyError:
                        print(f"Unknown brand '{brand_str}' in file. Skipping this car.")
                        continue

                    self.cars.append(Car(plate_number, brand, model, rate_per_day, availability))

        print(f"Loaded {len(self.cars)} car(s) from {filename}\n")
