cash = 1000000
currentPlane = None
class Plane:
    def __init__(self, name, price, capacity, range):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.range = range

    def __str__(self):
        return "%s, Price: %s, Capacity: %s, Range: %s" % (self.name, self.price, self.capacity, self.range)

B717 = Plane("Boing 717", 347000, 134, 2060)
A318 = Plane("Airbug A318", 520000, 132, 3570)
planes = [B717, A318]

def purchase(cash, currentPlane):
    print("Aircraft available for purchase:")
    for (i, plane) in enumerate(planes, start=1):
        print(i, plane)

    selectedPlane = int(input('Select aircraft\n')) - 1

    if cash - planes[selectedPlane].price > 0:
        print("You've selected %s" % (planes[selectedPlane].name))
        cash = cash - planes[selectedPlane].price
        print("You have %s remaining" % (cash))
        currentPlane = planes[selectedPlane].name
        return currentPlane
    else:
        print("Sorry, you do not have enough money to purchase this plane. Your current cash is %s" % (cash))
        return
        

    
def main(cash, currentPlane):
    print("""Actions:
          1. Purchase a plane
          2. Set up a flight""")
    action = int(input('Select an action\n'))
    if action == 1:
        currentPlane = purchase(cash, currentPlane)
        print("Selected plane is now %s" % (currentPlane))
    elif action == 2:
        print("This action is not supported yet.")

main(cash, currentPlane)