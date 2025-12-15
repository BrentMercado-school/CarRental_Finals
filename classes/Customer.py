class Customer:
    def __init__(self, customer_id, name, contact_number, rented_cars):
        self.customer_id = customer_id
        self.name = name
        self.contact_number = contact_number
        self.rented_cars = rented_cars

    def display_customer_details(self):
        print("Customer Details:")
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Contact Number: {self.contact_number}")

    def display_rented_cars(self):
        if not self.rented_cars:
            print("No rented cars.")
            return

        print("Customer Rented Cars:")
        for plate in self.rented_cars:
            print(f"- {plate}")

    def to_file_format(self):
        rented_cars_str = "|".join(self.rented_cars)
        return f"{self.customer_id},{self.name},{self.contact_number},{rented_cars_str}\n"
