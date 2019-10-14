import time
import math
from pymavlink import mavutil # Needed for command message definitions
from dronekit import connect, VehicleMode, LocationGlobalRelative

def condition_yaw(heading, relative=False):
    if relative:
        is_relative=1 #yaw relative to direction of travel
    else:
        is_relative=0 #yaw is an absolute angle
    # create the CONDITION_YAW command using command_long_encode()
    msg = vehicle.message_factory.command_long_encode(
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
        0, #confirmation
        heading,    # param 1, yaw in degrees
        0,          # param 2, yaw speed deg/s
        1,          # param 3, direction -1 ccw, 1 cw
        is_relative, # param 4, relative offset 1, absolute angle 0
        0, 0, 0)    # param 5 ~ 7 not used
    # send command to vehicle
    vehicle.send_mavlink(msg)
    
def arm_and_takeoff(aTargetAltitude):
    while not vehicle.is_armable:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:      
        print " Waiting for arming..."
        time.sleep(1)

    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude)
    # Wait for takeoff to finish
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt      
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: #Trigger just below target alt.
            print "Reached target altitude"
            break
        time.sleep(1)

def get_distance_metres(aLocation1, aLocation2):
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5

# define connection method 
# see all the methods at http://python.dronekit.io/guide/connecting_vehicle.html
connection_string = "127.0.0.1:14550"

# Connect
vehicle = connect(connection_string, wait_ready=True)
# arm and takeooff to 10m
arm_and_takeoff(10)
# set airspeed to 3 m/s
vehicle.airspeed = 3

point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
vehicle.simple_goto(point1)

targetDistance = 100

while vehicle.mode.name=="GUIDED": #Stop action if we are no longer in guided mode.
        remainingDistance = get_distance_metres(vehicle.location.global_frame, point1)
        print "Distance to target: ", remainingDistance
        if remainingDistance<=targetDistance*0.01: #Just below target, in case of undershoot.
            print "Reached target"
            break;
        time.sleep(2)


condition_yaw(170)

time.sleep(20)
vehicle.mode = VehicleMode("LAND")
time.sleep(20)
#Close vehicle object before exiting script
print "Close vehicle object"
vehicle.close()