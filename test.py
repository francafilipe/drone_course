from dronekit import LocationGlobal, LocationGlobalRelative
from connect import connectCopter
from arm_takeoff import armCopter, takeoffCopter
from goto import goto
import argparse

# ------------------ Main Executable ------------------
# Creating a argument that enables the ip address to be parsed from the command line 
parser = argparse.ArgumentParser(description='commands')
parser.add_argument('--connect')
args = parser.parse_args()
conn_ip = args.connect

# Calls the connectCopter function that initilize a copter vehicle and connects to it
copter = connectCopter(conn_ip)

# Calls the armCopter function responsible to arm the vehicle
armCopter(copter)

# Takeoff
while True:
    tk_option = input('Proceed to Takeoff? [Y/N] ').upper()
    if tk_option=='Y' or tk_option=='N':
        break
    else:
        print('Input not valid!')

if tk_option=='Y':
    targetHeight = int(input('Desired Takeoff Height [m]: '))
    takeoffCopter(copter,targetHeight)

# Flying to Waypoint
print('Initializing Mission')
wp1 = LocationGlobalRelative(-20.5399243538212,-47.36084905761948,30)

goto(copter,wp1)
