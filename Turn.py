
import time
import math
from Tools import ArduTools
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

def nav_change_heading(angle):

    direction = 1 if angle > 0 else -1

    heading = math.fabs(angle)

    target = vehicle.heading + angle

    target = target if target < 360 else target - 360
    target = target if target > 0 else target + 360

    # create the CONDITION_YAW command using command_long_encode()
    msg = vehicle.message_factory.command_long_encode(
        0, 0,       # target system, target component
        mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
        0,          #confirmation
        heading,    # param 1, yaw in degrees
        0,          # param 2, yaw speed deg/s
        direction,  # param 3, direction -1 ccw, 1 cw
        1,          # param 4, relative offset 1, absolute angle 0
        0, 0, 0)    # param 5 ~ 7 not used
    # send command to vehicle
    vehicle.send_mavlink(msg)

    # Wait for takeoff to finish
    print "Target heading ", target
    #while True:
    while not ArduTools.hasReachedHeading(vehicle.heading, target):
        print " Heading: ", vehicle.heading     
        #if vehicle.heading >= target-2 and vehicle.heading <= target+2: #Trigger just below target alt.
        #    print "Reached target heading"
        #    break
        time.sleep(1)
    print "Reached heading ", vehicle.heading

def nav_goto_heading(heading, cw = True):

    direction = 1 if cw else -1

    # create the CONDITION_YAW command using command_long_encode()
    msg = vehicle.message_factory.command_long_encode(
        0, 0,       # target system, target component
        mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
        0,          #confirmation
        heading,      # param 1, yaw in degrees
        0,          # param 2, yaw speed deg/s
        direction,  # param 3, direction -1 ccw, 1 cw
        0,          # param 4, relative offset 1, absolute angle 0
        0, 0, 0)    # param 5 ~ 7 not used
    # send command to vehicle
    vehicle.send_mavlink(msg)

    print "Target heading ", heading
    while not ArduTools.hasReachedHeading(vehicle.heading, heading):
        print " Heading: ", vehicle.heading     
        # if vehicle.heading >= target-2 and vehicle.heading <= target+2: #Trigger just below target alt.
        #     print "Reached target heading"
        #     break
        time.sleep(1)
    print "Reached heading ", vehicle.heading

def change_altitute(altitude):

    if(vehicle.mode.name == 'GUIDED' and vehicle.armed == True):
        current_loc = vehicle.location.global_relative_frame #get current location
        aTargetAltitude = current_loc.alt + altitude
        target_loc = LocationGlobalRelative(current_loc.lat, current_loc.lon, aTargetAltitude)
        
        vehicle.simple_goto(target_loc)

        # Wait for takeoff to finish
        while True:
            print " Altitude: ", vehicle.location.global_relative_frame.alt      
            if vehicle.location.global_relative_frame.alt >= aTargetAltitude*0.95 and vehicle.location.global_relative_frame.alt <= aTargetAltitude*1.05: #Trigger just below target alt.
                print "Reached target altitude"
                break
            time.sleep(1)

    else:
        print "Not armed or in GUIDED mode"

def goto_altitute(aTargetAltitude):

    if(vehicle.mode.name == 'GUIDED' and vehicle.armed == True):
        current_loc = vehicle.location.global_relative_frame #get current location
        target_loc = LocationGlobalRelative(current_loc.lat, current_loc.lon, aTargetAltitude)
        
        vehicle.simple_goto(target_loc)

        # Wait for takeoff to finish
        while True:
            print " Altitude: ", vehicle.location.global_relative_frame.alt      
            if vehicle.location.global_relative_frame.alt >= aTargetAltitude*0.95 and vehicle.location.global_relative_frame.alt <= aTargetAltitude*1.05: #Trigger just below target alt.
                print "Reached target altitude"
                break
            time.sleep(1)
    else:
        print "Not armed or in GUIDED mode"

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


def land():
    vehicle.mode = VehicleMode("LAND")
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt      
        if vehicle.location.global_relative_frame.alt <= 0.05: #Trigger just below target alt.
            print "Landed"
            break
        time.sleep(1)
    time.sleep(5)
    print "Close vehicle object"
    vehicle.close()

# define connection method 
# see all the methods at http://python.dronekit.io/guide/connecting_vehicle.html
connection_string = "127.0.0.1:14550"

# Connect
vehicle = connect(connection_string, wait_ready=True)
# arm and takeooff to 10m
arm_and_takeoff(5)
# set airspeed to 3 m/s
vehicle.airspeed = 3


# print "Change altitude by +5"
# change_altitute(5)
# time.sleep(5)

# print "Go to altitude 3"
# goto_altitute(3)
# time.sleep(5)

# print "Change altitude by +12"
# change_altitute(12)
# time.sleep(5)

# print "Change altitude by -5"
# change_altitute(-5)
# time.sleep(5)




print "Change heading by -15"
nav_change_heading(-125)
time.sleep(5)

# print "Change heading by -75"
# nav_change_heading(-75)
# time.sleep(5)


# print "Change heading by -95"
# nav_change_heading(-95)
# time.sleep(5)


# print "Change heading by 100"
# nav_change_heading(100)
# time.sleep(5)


# print "Change heading by 25"
# nav_change_heading(25)
# time.sleep(5)


# print "Change heading by 250"
# nav_change_heading(250)
# time.sleep(5)






# print "Change heading to 0"
# nav_goto_heading(0)
# time.sleep(5)

# print "Change heading by -15"
# nav_change_heading(-15)
# time.sleep(5)

# print "Change heading by -30"
# nav_change_heading(-30)
# time.sleep(5)

# print "Change heading by 45"
# nav_change_heading(45)
# time.sleep(5)

# print "Change heading to 245"
# nav_goto_heading(245)
# time.sleep(5)


# print "Change heading by 0"
# nav_change_heading(0)
# time.sleep(5)

# print "Change heading to 0"
# nav_goto_heading(0)
# time.sleep(5)


# print "Turn to 0"
# condition_yaw(0)
# time.sleep(5)

# print "Turn to 45"
# condition_yaw(45)
# time.sleep(5)

# print "Turn to 90"
# condition_yaw(90)
# time.sleep(5)

# print "Turn to 270"
# condition_yaw(270)
# time.sleep(5)

# print "Turn to 30"
# condition_yaw(30)
# time.sleep(5)

# print "Turn to 0"
# condition_yaw(0)
# time.sleep(5)


# print "Turn relative by 15"
# condition_yaw(15, True)
# time.sleep(5)

# print "Turn relative by 30:45"
# condition_yaw(30, True)
# time.sleep(5)

# print "Turn relative by 135:180"
# condition_yaw(135, True)
# time.sleep(5)

# print "Turn relative by 180:360"
# condition_yaw(180, True)
# time.sleep(5)

# print "Turn relative by 90:90"
# condition_yaw(90, True)
# time.sleep(5)

# print "Turn relative by 270:360"
# condition_yaw(270, True)
# time.sleep(5)


land()