# ------------- Importing Dependencies -------------
from dronekit import connect

# -------- Function to Connect to a vehicle --------
def connectCopter(conn_ip):
    # Connects to a drone listening in the conn_ip IP address
    copter = connect(conn_ip,wait_ready=True)

    return copter
