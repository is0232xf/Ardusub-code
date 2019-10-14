import time
from ArduPilotDriver import ArduPilotDriver

UAV = ArduPilotDriver()

UAV.start()


UAV.takeoff(5)

print("")
print("#################################################################")
print("# Test move to coordinates")

# print("")
# print ">>Move to lat, lon (-35.3630, 149.165218)"
# UAV.setAirSpeed(5)
# UAV.nav_goto_gps_coordinates(-35.3630, 149.165218)
# time.sleep(2)

print("")
print (">>Move to x, y (-20, 20)")
UAV.setAirSpeed(5)
UAV.nav_goto_gps_xy_NE_coordinates(-20, 20)
print("Succeeded")
time.sleep(2)

print("")
print(">>Move to x, y (20, 20)")
UAV.setAirSpeed(5)
UAV.nav_goto_gps_xy_NE_coordinates(20, 20)
print("Succeeded")
time.sleep(2)

print("")
print("#################################################################")
print("# Return to Home")

print("")
print (">>Return")
UAV.setAirSpeed(3)
UAV.returnToHome()

#print("")
#print("#################################################################")
#print("# Land")

#UAV.land()

UAV.exit()