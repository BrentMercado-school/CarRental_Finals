import os

from classes.Customer import Customer
from utils.Helper import get_non_empty_input, get_valid_integer


class CustomerManagement:
    def __init__(self):
        self.customers = []
        self.next_customer_id = 1

    def add_customer(self):
        name = get_non_empty_input("Enter customer name", "'Customer Name' should not be empty")
        contact_number = get_valid_integer("Enter contact number", "Please enter a valid whole number")
        rented_cars = []

        self.customers.append(Customer(self.next_customer_id, name, contact_number, rented_cars))
        self.next_customer_id += 1

        print(f"Successfully added customer '{name}'")

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def remove_customer(self):
        customer_id = get_valid_integer("Enter customer ID", "Please enter a valid customer ID")
        customer = self.get_customer_by_id(customer_id)

        if customer is None:
            print("Customer not found")
            return

        if customer.rented_cars:
            print("Cannot remove customer with active rentals.")
            return

        self.customers.remove(customer)
        print(f"Successfully removed customer '{customer.name}'")

    def display_customers(self):
        if len(self.customers) == 0:
            print("Customer list is empty")
            return
        for customer in self.customers:
            customer.display_customer_details()

    def update_customer(self):
        customer_id = get_valid_integer("Enter customer ID", "Please enter a valid customer ID")
        customer = self.get_customer_by_id(customer_id)

        if customer is None:
            print("Customer not found")
            return

        print(f"Press ENTER to keep current details of {customer.name}.")

        name_input = input(f"Enter new customer name (current: {customer.name}): ").strip()
        if name_input == "":
            new_name = customer.name
        else:
            new_name = name_input

        contact_input = input(f"Enter new contact number (current: {customer.contact_number}): ").strip()

        if contact_input == "":
            new_contact_number = customer.contact_number
        else:
            try:
                new_contact_number = int(contact_input)
            except ValueError:
                print("Invalid contact number.")
                return

        customer.name = new_name
        customer.contact_number = new_contact_number
        print("Successfully updated customer details.")

    def search_customer(self):
        customer_name = input("Enter customer name: ").strip()
        founded_customers = []
        for customer in self.customers:
            if customer_name.lower() in customer.name.lower():
                founded_customers.append(customer)

        if len(founded_customers) == 0:
            print("Customer not found")
            return

        print(f"Founded {len(founded_customers)} customers with name '{customer_name}'.")
        for customer in founded_customers:
            customer.display_customer_details()

    def save_file(self, filename):
        with open(filename, "w") as file:
            for customer in self.customers:
                file.write(customer.to_file_format())

        print(f"Saved {len(self.customers)} customer(s) to {filename}.")

    def load_file(self, filename):
        self.customers = []

        try:
            if not os.path.exists(filename):
                print(f"No existing {filename} found. Starting with an empty list.\n")

            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()

                    if line == "":
                        continue

                    parts = line.split(",")

                    customer_id = int(parts[0])
                    name = parts[1]
                    contact_number = int(parts[2])

                    if len(parts) > 3 and parts[3] != "":
                        rented_cars = parts[3].split("|")
                    else:
                        rented_cars = []

                    self.customers.append(
                        Customer(customer_id, name, contact_number, rented_cars)
                    )

            if self.customers:
                self.next_customer_id = max(c.customer_id for c in self.customers) + 1
            else:
                self.next_customer_id = 1
            print(f"Loaded {len(self.customers)} customer(s) from {filename}.")

        except FileNotFoundError:
            pass

    def add_temp_customer(self):
        self.customers.append(Customer(1, "Brent", 121211,
                                       []))


