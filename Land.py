import time
import math

from dronekit import connect, VehicleMode, LocationGlobalRelative

# define connection method 
# see all the methods at http://python.dronekit.io/guide/connecting_vehicle.html
connection_string = "127.0.0.1:14550"

# Connect
vehicle = connect(connection_string, wait_ready=True)
# arm and takeooff to 10m
#arm_and_takeoff(10)
# set airspeed to 3 m/s
#vehicle.airspeed = 3

vehicle.mode = VehicleMode("LAND")
vehicle.armed = True