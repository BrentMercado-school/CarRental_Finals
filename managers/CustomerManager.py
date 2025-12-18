import os
from tabulate import tabulate

from classes.Customer import Customer
from utils.Helper import get_non_empty_input, get_valid_integer


class CustomerManagement:
    def __init__(self):
        self.customers = []
        self.next_customer_id = 1

    def add_customer(self):
        print("\n" + "=" * 45)
        print("        ADD NEW CUSTOMER")
        print("=" * 45)

        name = get_non_empty_input(
            "Enter customer name",
            "Customer name should not be empty."
        )

        contact_number = get_valid_integer(
            "Enter contact number",
            "Please enter a valid whole number."
        )

        rented_cars = []

        self.customers.append(
            Customer(self.next_customer_id, name, contact_number, rented_cars)
        )
        print("\n" + "=" * 45)
        print("Customer added successfully!")
        print("-" * 45)
        print(f"Customer ID    : {self.next_customer_id}")
        print(f"Name           : {name}")
        print(f"Contact Number : {contact_number}")
        print("=" * 45)

        self.next_customer_id += 1
        input("Press enter to continue...")

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def remove_customer(self):
        if len(self.customers) == 0:
            print("Customer list is empty.")
            return

        print("\n" + "=" * 45)
        print("        REMOVE CUSTOMER")
        print("=" * 45)

        customer_id = get_valid_integer(
            "Enter customer ID to remove",
            "Please enter a valid customer ID."
        )

        customer = self.get_customer_by_id(customer_id)

        if customer is None:
            print("\nCustomer not found.")
            return

        if customer.rented_cars:
            print("\nCannot remove customer with active rentals.")
            print(f"Customer has {len(customer.rented_cars)} rented car(s).")
            return

        print("\nCUSTOMER DETAILS")
        print("-" * 45)
        print(f"Customer ID    : {customer.customer_id}")
        print(f"Name           : {customer.name}")
        print(f"Contact Number : {customer.contact_number}")

        confirm = input(f"\nAre you sure you want to remove this customer? (Y/N): ").strip().upper()
        if confirm != "Y":
            print("\nCustomer removal canceled.")
            return

        self.customers.remove(customer)

        print("\n" + "=" * 45)
        print(f"Customer '{customer.name}' removed successfully.")
        print("=" * 45)

    def display_customers(self):
        if len(self.customers) == 0:
            print("Customer list is empty.")
            return

        data = []

        for customer in self.customers:
            data.append({
                "Customer ID": customer.customer_id,
                "Name": customer.name,
                "Contact Number": customer.contact_number,
                "Rented Cars": len(customer.rented_cars)
            })

        print("CUSTOMER LIST")

        table = tabulate(data, headers="keys", tablefmt="pipe")
        print(table)

        input("Press enter to continue...")

    def update_customer(self):
        if len(self.customers) == 0:
            print("Customer list is empty.")
            return

        print("\n" + "=" * 45)
        print("        UPDATE CUSTOMER DETAILS")
        print("=" * 45)

        customer_id = get_valid_integer(
            "Enter customer ID to update",
            "Please enter a valid customer ID."
        )

        customer = self.get_customer_by_id(customer_id)

        if customer is None:
            print("\nCustomer not found.")
            return

        print("\nCURRENT CUSTOMER DETAILS")
        print("-" * 45)
        print(f"Customer ID    : {customer.customer_id}")
        print(f"Name           : {customer.name}")
        print(f"Contact Number : {customer.contact_number}")

        print("\nPress ENTER to keep the current value.")

        name_input = input(f"\nEnter new customer name (current: {customer.name}): ").strip()
        new_name = customer.name if name_input == "" else name_input

        contact_input = input(f"Enter new contact number (current: {customer.contact_number}): ")
        if contact_input == "":
            new_contact_number = customer.contact_number
        else:
            try:
                new_contact_number = int(contact_input)
            except ValueError:
                print("\nInvalid contact number. Update canceled.")
                return

        customer.name = new_name
        customer.contact_number = new_contact_number

        print("\n" + "=" * 45)
        print("Customer details updated successfully!")
        print("-" * 45)
        print(f"Customer ID    : {customer.customer_id}")
        print(f"Name           : {customer.name}")
        print(f"Contact Number : {customer.contact_number}")
        print("=" * 45)

        input("Press enter to continue...")

    def search_customer(self):
        print("\n" + "=" * 45)
        print("        SEARCH CUSTOMERS")
        print("=" * 45)

        if len(self.customers) == 0:
            print("\nCustomer list is empty.")
            return

        customer_name = input("\nEnter customer name to search: ").strip()

        found_customers = [
            customer for customer in self.customers
            if customer_name.lower() in customer.name.lower()
        ]

        if not found_customers:
            print(f"\nNo customers found with name '{customer_name}'.")
            return

        data = []
        for customer in found_customers:
            data.append({
                "Customer ID": customer.customer_id,
                "Name": customer.name,
                "Contact Number": customer.contact_number,
                "Rented Cars": len(customer.rented_cars)
            })

        print("\n" + "=" * 45)
        print(f"Found {len(found_customers)} customer(s) with name '{customer_name}'")
        print("=" * 45)
        print(tabulate(data, headers="keys", tablefmt="pipe"))

        input("Press enter to continue...")

    def save_file(self, filename):
        with open(filename, "w") as file:
            for customer in self.customers:
                file.write(customer.to_file_format())

        print(f"Saved {len(self.customers)} customer(s) to {filename}.\n")

    def save_file_rented(self, filename):
        with open(filename, "w") as file:
            for customer in self.customers:
                file.write(customer.to_file_format())

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


