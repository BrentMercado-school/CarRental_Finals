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
            "Car brand should not be blank."
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
        print(f"No car with plate number {plate_number}")
        return None

    def remove_car(self):
        plate_number = get_non_empty_input("Enter plate number", "Invalid input")
        car = self.get_car_by_plate_number(plate_number)

        self.cars.remove(car)
        print(f"Successfully removed car {plate_number} from car management.")

    def display_cars(self):
        for car in self.cars:
            car.display_car_details()

    def add_test_car(self):
        self.cars.append(Car("a", CarBrand.TOYOTA, "Vios", 1500, True))
        self.cars.append(Car("aa", CarBrand.TOYOTA, "Innova", 1500, True))
        self.cars.append(Car("BBB 222", CarBrand.HONDA, "Civic", 1800, True))
        self.cars.append(Car("CCC 333", CarBrand.MITSUBISHI, "Xpander", 2000, False))
        self.cars.append(Car("DDD 444", CarBrand.NISSAN, "Terra", 2500, True))

    def update_car(self):
        plate_number = get_non_empty_input("Enter plate number", "Invalid input")
        car = self.get_car_by_plate_number(plate_number)

        if car is None:
            return

        car.display_car_details()
        print(f"Press ENTER to keep current details of {car.plate_number}.")

        for brand in CarBrand:
            print(f"- {brand.value}")

        brand_input = input("Enter new car brand: ").strip().upper()

        if brand_input == "":
            new_brand = car.brand
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
            new_rate = car.rate_per_day
        else:
            try:
                new_rate = int(new_rate_input)
            except ValueError:
                print("Invalid rate. Update canceled.")
                return


        car.brand = new_brand
        car.model = new_model
        car.rate_per_day = new_rate

        print("Successfully updated car details.")

    # Search cars by brand, model, or availability
    # not done
    def search_cars(self):
        print("1 - Brand | 2 - Model | 3 - Availability | 4 - low to high | 5 - high to low")

        brand_input = input("Enter car brand: ").strip().upper()

        try:
            selected_brand = CarBrand[brand_input]
        except KeyError:
            print("Invalid brand. Car not added.")
            return

        filtered_cars = [car for car in self.cars if car.brand == selected_brand]

        for car in filtered_cars:
            car.display_car_details()

    # SAVE CARS TO FILE
    def save_file(self):
        pass

    # LOAD CARS FROM FILE
    def load_file(self):
        pass