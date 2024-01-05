from classes.plane import Plane
from database import *

cash = 1000000
currentPlane = None

# Manufacturer, Name, price, seats total, seats first class, cruise (knots), range, fuel (us gal, usable),
B717 = Plane("Boing","717-200", 347000, 106, 8, 444, 2060, 3679)
A318 = Plane("Airbug", "A318", 520000, 132, 0, 445, 3570, 6303)
planes = [B717, A318]

for plane in planes:
    insert_plane(plane)

boing = list_planes("Boing")
print(boing)

# def purchase(cash, currentPlane):
#     print("Aircraft available for purchase:")
#     for (i, plane) in enumerate(planes, start=1):
#         print(i, plane)

#     selectedPlane = int(input('Select aircraft\n')) - 1

#     if cash - planes[selectedPlane].price > 0:
#         print("You've selected %s" % (planes[selectedPlane].name))
#         cash = cash - planes[selectedPlane].price
#         print("You have %s remaining" % (cash))
#         currentPlane = planes[selectedPlane].name
#         return currentPlane
#     else:
#         print("Sorry, you do not have enough money to purchase this plane. Your current cash is %s" % (cash))
#         return
        

    
# def main(cash, currentPlane):
#     print("""Actions:
#           1. Purchase a plane
#           2. Set up a flight""")
#     action = int(input('Select an action\n'))
#     if action == 1:
#         currentPlane = purchase(cash, currentPlane)
#         print("Selected plane is now %s" % (currentPlane))
#     elif action == 2:
#         print("This action is not supported yet.")

# main(cash, currentPlane)
close_connection()