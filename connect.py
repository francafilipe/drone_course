# Importing Dependencies
from dronekit import *
import time
import socket
import exceptions
import math
import argparse

# Functions

def connectCopter(connection_ip):
    vehicle = connect(connection_ip,wait_ready=True)
    return vehicle

# Main Executable

# Get arguments passed in the command line
parser = argparse.ArgumentParser(description='commads')     # creat an ArgumentParser object (used to handle information to parse command line into Python data)
parser.add_argument('--connect')    # create an argument --connect that can be used to parse the ip address of the drone by command line 
args = parser.parse_args()          # parse_args will inspect the command line and convert eaach argument to the appropriate type and then invoke the appropriate action
                                    # in this case, an Namespace connect is built to hold the ip address parsed out of the command line

connection_ip = args.connect        # set the connection_ip variable as the string parsed out of the command line using the --connect argument

# Call to connect function - connects the script to the drone using the IP address passed 
vehicle = connectCopter(connection_ip)
