#dito na ung ui interaction sa user
from managers.CarManager import CarManager
from utils.Helper import display_cars_menu, display_main_menu, search_car_prompt, display_customer_menu, \
    display_rental_menu, display_report_menu

print("hello -JC")

#filenames
car_filename = "cars.txt"
customer_filename = "customers.txt"
rental_filename = "rentals.txt"

#load data from files (cars, customers, rentals)
car_manager = CarManager()
car_manager.load_file(car_filename)

while True:
    display_main_menu()
    main_menu_choice = input("Enter your choice: ")

    while True:
        #Dito na ung lahat ng functions ng cars
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

        #Dito na ung lahat ng functions ng customers
        elif main_menu_choice == "2":
            display_customer_menu()

        # Dito na ung lahat ng functions ng pag rerent ng car
        elif main_menu_choice == "3":
            display_rental_menu()

        # Dito na ung lahat ng functions ng report
        elif  main_menu_choice == "4":
            display_report_menu()






