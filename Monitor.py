
import time
from ArduPilotDriver import ArduPilotDriver

UAV = ArduPilotDriver()

UAV.connection_string = "0.0.0.0:14560"

UAV.start()

while True:
    print ("")
    print("Heading ", UAV.vehicle.heading)
    print ("Global Location: %s" % UAV.vehicle.location.global_frame)
    print ("Global Location (relative altitude): %s" % UAV.vehicle.location.global_relative_frame)
    print ("Local Location: %s" % UAV.vehicle.location.local_frame)    #NED
    print ("Attitude: %s" % UAV.vehicle.attitude)
    print("Velocity ", UAV.vehicle.velocity)
    print("Groud Speed ", UAV.vehicle.groundspeed)
    print("Air Speed ", UAV.vehicle.airspeed)
    print("Battery ", UAV.vehicle.battery)
    print ("EKF OK?: %s" % UAV.vehicle.ekf_ok)
    print ("Last Heartbeat: %s" % UAV.vehicle.last_heartbeat)
    print ("System status: %s" % UAV.vehicle.system_status.state)
    print ("Mode: %s" % UAV.vehicle.mode.name)    # settable
    print ("Armed: %s" % UAV.vehicle.armed)    # settable
    time.sleep(0.5)
