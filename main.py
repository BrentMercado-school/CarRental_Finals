from managers.CarManager import CarManager
from managers.CustomerManager import CustomerManagement
from managers.RentalManager import RentalManagement
from utils.Helper import display_cars_menu, display_main_menu, search_car_prompt, display_customer_menu, \
    display_rental_menu, display_report_menu

car_filename = "cars.txt"
customer_filename = "customers.txt"
rental_filename = "rentals.txt"

car_manager = CarManager()
customer_manager = CustomerManagement()
rental_manager = RentalManagement(customer_manager, car_manager)

car_manager.load_file(car_filename)
customer_manager.load_file(customer_filename)
rental_manager.load_file(rental_filename)

while True:
    display_main_menu()
    main_menu_choice = input("Enter your choice: ")

    while True:
        if main_menu_choice == "1":
            display_cars_menu()
            cars_menu_choice = input("Enter your choice: ")

            if cars_menu_choice == "1":
                car_manager.add_car()

            elif cars_menu_choice == "2":
                car_manager.display_cars()

            elif cars_menu_choice == "3":
                car_manager.update_car()

            elif cars_menu_choice == "4":
                car_manager.remove_car()

            elif cars_menu_choice == "5":
                search_choice = search_car_prompt()

                if search_choice == "1":
                    car_manager.search_by_brand()
                elif search_choice == "2":
                    car_manager.search_by_model()
                elif search_choice == "3":
                    car_manager.search_by_availability()
                else:
                    print("Invalid choice")

            elif cars_menu_choice == "6":
                car_manager.save_file(car_filename)

            elif cars_menu_choice == "7":
                break

            else:
                print("Invalid choice")
                continue

        elif main_menu_choice == "2":
            display_customer_menu()
            customer_menu_choice = input("Enter your choice: ")

            if customer_menu_choice == "1":
                customer_manager.add_customer()
            elif customer_menu_choice == "2":
                customer_manager.display_customers()
            elif customer_menu_choice == "3":
                customer_manager.update_customer()
            elif customer_menu_choice == "4":
                customer_manager.remove_customer()
            elif customer_menu_choice == "5":
                customer_manager.search_customer()
            elif customer_menu_choice == "6":
                customer_manager.save_file(customer_filename)
            elif customer_menu_choice == "7":
                break
            else:
                print("Invalid choice")
                continue

        elif main_menu_choice == "3":
            display_rental_menu()
            rental_menu_choice = input("Enter your choice: ")

            if rental_menu_choice == "1":
                rental_manager.rent_car()
            elif rental_menu_choice == "2":
                rental_manager.return_car()
            elif rental_menu_choice == "3":
                rental_manager.display_rentals()
            elif rental_menu_choice == "4":
                rental_manager.display_rentals_by_customer()
            elif rental_menu_choice == "5":
                rental_manager.save_file(rental_filename)
            elif rental_menu_choice == "6":
                break
            else:
                print("Invalid choice")
                continue

        elif  main_menu_choice == "4":
            display_report_menu()
            report_menu_choice = input("Enter your choice: ")

            if report_menu_choice == "1":
                car_manager.search_by_availability()
            elif report_menu_choice == "2":
                rental_manager.search_by_rented_cars()
            elif report_menu_choice == "3":
                rental_manager.search_by_returned_cars()
            elif report_menu_choice == "4":
                break
            else:
                print("Invalid choice")
                continue






