class Plane:
    def __init__(self, manufacturer, name, price, seats, fcseats, cruise, range, fuel, runway):
        self.manufacturer = manufacturer
        self.name = name
        self.price = price
        self.seats = seats
        self.fcseats = fcseats
        self.cruise = cruise
        self.range = range
        self.fuel = fuel
        self.runway = runway

    def __str__(self):
        return ":manufacturer :name, Price: :price\n :seats of seats, :fcseats of which are first class\n :name has a cruising speed of :cruise, with a range of :range nautical miles and :fuel gallons of fuel.", {'manufacturer':self.manufacturer, 'name':self.name, 'price':self.price, 'seats':self.seats, 'fcseats':self.fcseats, 'cruise':self.cruise, 'range':self.range, 'fuel':self.fuel}