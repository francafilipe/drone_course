# ------------- Importing Dependencies -------------
from dronekit import VehicleMode
from math import sqrt
from time import sleep

# Land function - lands the vehicle after reaching a landing waypoint
def land(vehicle):
    vehicle.mode = VehicleMode('LAND')
    while vehicle.mode!="LAND":
        print('Waiting vehicle to enter LAND Mode')
        sleep(1)
    print('Vehicle in LAND Mode')
