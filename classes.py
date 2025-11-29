# CAR
from enums import *
class Car:
    def __init__(self, plate_number, brand, model, rate_per_day, availability):
        self.plate_number = plate_number
        self.brand = brand
        self.model = model
        self.rate_per_day = rate_per_day
        self.availability = availability

    def display_car_details(self):
        print(f"Plate Number: {self.plate_number} | Brand: {self.brand} | Model: {self.model}"
              f"Rate: {self.rate_per_day} | Availability: {self.availability}")

    def is_available(self):
        pass

class CarManagement:
    def __init__(self):
        self.cars = []

    # mga main functions na naiisip ko pero pwede niyo bawasan or dagdagan
    # ADD NEW CAR
    def add_car(self):
        pass

    # GET CAR BY PLATE NO.
    def get_car_by_plate_number(self):
        pass

    # REMOVE CAR
    def remove_car(self):
        pass

    # DISPLAY ALL CARS
    def display_cars(self):
        pass

    # UPDATE CAR DETAILS
    def update_car(self):
        pass

    # Search cars by brand, model, or availability
    def search_car(self):
        pass

    # SAVE CARS TO FILE
    def save_file(self):
        pass

    # LOAD CARS FROM FILE
    def load_file(self):
        pass

#CUSTOMER
class Customer:
    # Attributes: Customer ID (primary key), Name, Contact Number, Rented Cars
    def __init__(self, customer_id, name, contact_number, rented_cars):
        pass

    # You can add other customer related functions here or any methods na related sa customer class natin
    # Example lang yang mga nilagay ko
    def display_customer_details(self):
        pass
    def display_rented_cars(self):
        pass
class CustomerManagement:
    def __init__(self):
        self.customers = []

    # mga main functions na naiisip ko pero pwede niyo bawasan or dagdagan
    # Add a new customer
    def add_customer(self):
        pass

    # Get customer by ID
    def get_customer_by_id(self):
        pass

    # Remove a customer
    def remove_customer(self):
        pass

    # Display all customers
    def display_customers(self):
        pass

    # Update customer details
    def update_customer(self):
        pass

    # Search customers by name
    def search_customer(self):
        pass

    # Save customers to file
    def save_file(self):
        pass

    # Load customers from file
    def load_file(self):
        pass

#RENTAL
class Rental:
    # Attributes: Rental ID, Customer ID, Car Plate Number, Number of Days, Total Cost, Status, Rental Date
    def __init__(self, rental_id, customer_id, car_plate, days, total_cost, status):
        pass

    # You can add other rental related functions here or any methods na related sa rental class natin
    # Example lang yang mga nilagay ko
    def display_rental_details(self):
        pass
    def calculate_total(self, rate_per_day, days):
        pass
    def mark_returned(self):
        pass
class RentalManagement:
    def __init__(self):
        self.rentals = []
        pass
    # mga main functions na naiisip ko pero pwede niyo bawasan or dagdagan
    # Rent a car
    def rent_car(self):
        pass

    # Return a car
    def return_car(self):
        pass

    # Get rental by ID
    def get_rental_by_id(self):
        pass

    # Display all rentals
    def display_rentals(self):
        pass

    # Display rentals per customer
    def display_rentals_by_customer(self):
        pass

    # Search rentals by car, customer, or status
    def search_rentals(self):
        pass

    # Save rentals to file
    def save_file(self):
        pass

    # Load rentals from file
    def load_file(self):
        pass
