# ------------- Importing Dependencies -------------
from dronekit import VehicleMode
import time

# ---- Function to arm and takeoff the vehicle -----
def armCopter(copter):

    while copter.is_armable!=True:
        print('Waiting for copter to become armable')
        time.sleep(1)
    print('\ncopter is armable')

    copter.mode = VehicleMode('GUIDED')
    while copter.mode!='GUIDED':
        print('Waiting for the copter to enter GUIDED mode')
        time.sleep(1)
    print('copter in GUIDED mode')

    copter.armed = True
    while copter.armed!=True:
        print('Waiting copter to arm')
        time.sleep(1)
    print('copter is armed')

    return None

def takeoffCopter(copter,targetHeight):
    copter.simple_takeoff(targetHeight)
    while True:
        print('Altitude: %d'%copter.location.global_relative_frame.alt)
        if copter.location.global_relative_frame.alt>=.95*targetHeight:
            break
        time.sleep(1)
    
    print('\nTakeoff Complete. Altitude: %d'%copter.location.global_relative_frame.alt)

    return None
