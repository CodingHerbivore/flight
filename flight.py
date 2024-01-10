from classes.plane import Plane
from db_setup import *
from database import *

load_planes()

cash = 1000000

def purchase(cash):
    print("Aircraft available for purchase:")
    
    available_planes = list_planes(0)

    for plane in available_planes:
        line = f'{plane[0]} {plane[1]}, Price: {plane[2]} {plane[3]} of seats, {plane[4]} of which are first class\n {plane[1]} has a cruising speed of {plane[5]}, with a range of {plane[6]} nautical miles and {plane[7]} gallons of fuel.\n\n'
        
        print(line)

    selectedPlane = int(input('Select aircraft\n')) - 1

    if cash - planes[selectedPlane].price > 0:
        print("You've selected %s" % (planes[selectedPlane].name))
        cash = cash - planes[selectedPlane].price
        print("You have %s remaining" % (cash))
        
    else:
        print("Sorry, you do not have enough money to purchase this plane. Your current cash is %s" % (cash))
        return
        

    
def main(cash):
    print("""Actions:
          1. Purchase a plane
          2. Set up a flight""")
    action = int(input('Select an action\n'))
    if action == 1:
        purchase(cash)
    elif action == 2:
        print("This action is not supported yet.")

main(cash)

close_connection()