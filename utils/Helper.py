import random
import string

#dito lagay natin mga helper methods natin for example:
def display_main_menu():
    print("MAIN MENU")
    print("1. Manage Cars\n2. Manage Customers\n3. Rental Transactions\n4. Reports\n5. Exit")

def display_cars_menu():
    print("--- Manage Cars ---")
    print("1. Add Car\n2. View All Cars\n3. Edit Car\n4. Remove Car\n5. Search Cars\n6. Save\n7. Back")

def display_customer_menu():
    print("Manage Customers")
    print("1. Add Customer\n2. View All Customer\n3. Edit Customer\n4. Remove Customer\n5. Search Customer\n6. Back")

def display_rental_menu():
    print("Rental  Transactions")
    print("1. Rent Car\n2. Return Car\n3. View All Rentals\n4. View Rentals  by  Customer\n5. Back")

def display_report_menu():
    print("Reports")
    print("1. Available Cars  Report\n2. Rented Cars Report\n3. Customer Rental History\n4. Complete Rental History\n5. Back")

def generate_plate_number():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=3))
    return f"{letters} {numbers}"

def get_non_empty_input(prompt, error_msg):
    user_input = input(f"{prompt}: ").strip()
    while user_input == "":
        print(f"\n{error_msg}")
        user_input = input(f"{prompt}: ").strip()
    return user_input

def get_valid_integer(prompt, error_msg):
    while True:
        user_input = input(f"{prompt}: ").strip()
        if user_input.isdigit():
            return int(user_input)
        print(f"\n{error_msg}")

def search_car_prompt():
    print("Search Cars By:")
    print("1. Brand\n2. Model\n3. Availability\n4. Back")
    return input("Enter your choice: ").strip()