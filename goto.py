# ------------- Importing Dependencies -------------
from dronekit import VehicleMode
from math import sqrt
from time import sleep

# Function to get the distance between the current location and the desired location
def distance(targetLoc,currentLoc):
    dist_Lat = targetLoc.lat - currentLoc.lat
    dist_Lon = targetLoc.lon - currentLoc.lon
    dist = sqrt(dist_Lat**2 + dist_Lon**2)

    return dist

# Go To function - takes a waypoint and flies the vehicle to that point
def goto(vehicle,wp):
    distTarget = distance(wp,vehicle.location.global_relative_frame)
    vehicle.simple_goto(wp)

    while vehicle.mode.name=="GUIDED":
        currentDistTarget = distance(wp,vehicle.location.global_relative_frame)
        if currentDistTarget<0.05*distTarget:
            print("Waypoint reached")
            sleep(1)
            break
        sleep(2)

    return None
