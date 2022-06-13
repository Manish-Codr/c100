class Car(object):
    def __init__(self, color, model, company, topspeed, horsepower):
        self.color = color
        self.model = model
        self.company = company
        self.topspeed = topspeed
        self.horsepower = horsepower

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def changeGear(self):
        print("gear changed")


audi = Car("Red", "A6", "Audi", "250", "100")


def newcar():
    color = input("Enter The Car Color: ")
    model = input("Enter The Car Model: ")
    company = input("Enter The Car Company: ")
    topspeed = input("Enter The Car Top Speed: ")
    horsepower = input("Enter The Car HorsePower: ")
    car = Car(color, model, company, topspeed, horsepower)
    print(car.color)
    print(car.model)
    print(car.company)
    print(car.topspeed)
    print(car.horsepower)


newcar()
