from dronekit import connect
from dronekit import VehicleMode
import time

print("start connecting")
connection_string = "udpin:0.0.0.0:14551"
print("connect to %s" % (connection_string))

vehicle =  connect(connection_string, wait_ready=True)

try:
    while True:
        # print vehicle state
        print("--------------------------" )
        print(" GPS: %s" % vehicle.gps_0 )
        print(" Battery: %s" % vehicle.battery )
        print(" Last Heartbeat: %s" % vehicle.last_heartbeat )
        print(" Is Armable?: %s" % vehicle.is_armable )
        print(" System status: %s" % vehicle.system_status.state )
        time.sleep(1)

# detect KeyboardInterrupt, close connection
except(KeyboardInterrupt, SystemExit):
    print( "detect SIGINT" )

vehicle.close()

print("finish the program") 