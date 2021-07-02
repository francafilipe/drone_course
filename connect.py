# ------------- Importing Dependencies -------------
from dronekit import connect

# -------- Function to Connect to a vehicle --------
def connectCopter(conn_ip):
    # Launches SITL drone if non IP address was explicitly specified
    if not conn_ip:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        conn_ip = sitl.connection_string()

    print(conn_ip)
    # Connects to a drone listening in the conn_ip IP address
    copter = connect(conn_ip,wait_ready=True)

    return copter
