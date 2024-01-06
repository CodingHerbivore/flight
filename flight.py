from classes.plane import Plane
from db_setup import *
from database import *

load_planes()

cash = 1000000
currentPlane = None



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