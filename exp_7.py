# Create a program that defines a class to represent a car and then create an object of that class with specific attributes and print out the details of the car
class Car:
    def info(self, brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details : {self.year},{self.brand},{self.model}")

car = Car()
car.info("Toyota", "Corolla", 2029)
car.display_details()