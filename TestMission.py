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
print (">>Move to way point 1")
UAV.setAirSpeed(0)
UAV.nav_goto_gps_coordinates(34.982122, 135.963603)
print("Succeeded")
time.sleep(30)

print("")
print(">>Move to way point 2")
UAV.setAirSpeed(0)
UAV.nav_goto_gps_coordinates(34.982180, 135.963606)
print("Succeeded")
time.sleep(30)

print("")
print (">>Move to way point 3")
UAV.setAirSpeed(0)
UAV.nav_goto_gps_coordinates(34.982184, 135.963684)
print("Succeeded")
time.sleep(30)

print("")
print("#################################################################")
print("# Return to Home")

print("")
print (">>Return")
UAV.setAirSpeed(0)
UAV.returnToHome()

#print("")
#print("#################################################################")
#print("# Land")

#UAV.land()

UAV.exit()