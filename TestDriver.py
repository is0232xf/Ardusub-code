import time
from Tools import ArduTools
from ArduPilotDriver import ArduPilotDriver
from dronekit import  LocationGlobalRelative, LocationGlobal



UAV = ArduPilotDriver()

UAV.start()

UAV.takeoff(5)

print("")
print("#################################################################")
print("# Test Altitude change")

# print("")
# print ">>Change altitude by +2"
# UAV.nav_change_altitute(2)
# time.sleep(5)

# print("")
# print ">>Goto altitude 2"
# UAV.nav_goto_altitute(2)
# time.sleep(5)

# print("")
# print("#################################################################")
# print("# Test heading change")

# print("")
# print ">>Change heading by 45"
# UAV.nav_change_heading(45)
# time.sleep(5)

# print("")
# print ">>Change heading to 0"
# UAV.nav_goto_heading(0)
# time.sleep(5)


print("")
print("#################################################################")
print("# Test move position")

# print("")
# print ">>Move nav_goto_gps_xycoordinates 5, 0"
# UAV.nav_goto_gps_xy_NE_coordinates(5,0)
# time.sleep(5)


# print("")
# print ">>Change heading by 45"
# UAV.nav_change_heading(45)
# time.sleep(5)


# print("")
# print(UAV.vehicle.heading)
# print ">>Move nav_goto_gps_xy_body_coordinates 5, 5"
# UAV.nav_goto_gps_xy_body_coordinates(5,20)
# time.sleep(5)

# print("")
# print ">>Move nav_move_distance_body  5, 0, 0"
# UAV.nav_move_distance_body(5, 0, 0)


# print("")
# print ">>Move velocity position 2, 2, 0, 5"
# UAV.nav_move_velocity_pos(2, 2, 0, 5)
# time.sleep(5)


# print("")
# print ">>Move velocity position 0, 0, 0"
# UAV.nav_move_velocity_pos(0, 0, 0)
# time.sleep(5)


# print("")
# print ">>Move nav_move_distance_body  100, 50, 0"
# UAV.nav_move_distance_body(100, 500, 0)

#time.sleep(1)


# print("")
# print ">>Change heading by 90"
# UAV.nav_change_heading(30)
# time.sleep(2)

# print("")
# print ">>Move velocity body 2, 1, 0, 5 "
# UAV.nav_move_velocity_body(2, 0, 0, 5)
# time.sleep(1)

# print("")
# print ">>Move velocity position 0, 0, 0"
# UAV.nav_move_velocity_pos(0, 0, 0)
# time.sleep(10)




print("")
print("#################################################################")
print("# Test area coverage")

#target = ArduTools.get_location_metres(UAV.vehicle.location.global_frame, 50, 50)
newlat = -35.363004
newlon = 149.166698
target = LocationGlobal(newlat, newlon, UAV.vehicle.location.global_frame.alt)

print (target)

points = ArduTools.calculate_boustrophedon_points(50, 10)

waypoints = []
for p in points:
    destination = ArduTools.get_location_metres(target, p[0], p[1])
    waypoints.append(destination)
    print (destination)
    UAV.nav_goto_gps_point(destination)

print(points)
print(waypoints)

time.sleep(5)

print("")
print("#################################################################")
print("# Return to home")

UAV.returnToHome()


# print("")
# print("#################################################################")
# print("# Land")

# UAV.land()

#UAV.exit()