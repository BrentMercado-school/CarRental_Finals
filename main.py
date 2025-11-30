#dito na ung ui interaction sa user
from managers.CarManager import CarManager

filename = "cars.txt"
car_manager = CarManager()

car_manager.load_file(filename)
car_manager.add_car()
car_manager.save_file(filename)
