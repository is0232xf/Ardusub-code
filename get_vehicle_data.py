"""
The code saves vehicle timestamp, attitude, GPS(position), 
output(pwm frequence value for each servo motor)as a csv file.

usage
$ python get_vehicle_data.py
"""

from pymavlink import mavutil
import time
import csv
import datetime

# Create the connection
master = mavutil.mavlink_connection('udp:0.0.0.0:14551')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Request all parameters
master.mav.param_request_list_send(
    master.target_system, master.target_component
)
# get date time object
detail = datetime.datetime.now()
date = detail.strftime("%Y_%m_%d_%H_%M_%S")
# open csv file
file = open('./csv/'+ date +'.csv', 'a', newline='')
csvWriter = csv.writer(file)
csvWriter.writerow(['time', 'latitude', 'longitide', 'roll', 'pitch', 'yaw', 'Servo_1', 'Servo_2', 'Servo_3', 'Servo_4'])

while True:
    time.sleep(0.1)
    try:
        GPS_message = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True).to_dict()
        attitude_message = master.recv_match(type='ATTITUDE', blocking=True).to_dict()
        servo_message = master.recv_match(type='SERVO_OUTPUT_RAW', blocking=True).to_dict()
        date = detail.strftime("%Y_%m_%d_%H_%M_%S")
        latitude = float(GPS_message['lat'])/10000000
        longitude = float(GPS_message['lon'])/10000000
        roll = float(attitude_message['roll'])
        pitch = float(attitude_message['pitch'])
        yaw = float(attitude_message['yaw'])

        servo_1 = int(servo_message['servo1_raw'])
        servo_2 = int(servo_message['servo2_raw'])
        servo_3 = int(servo_message['servo3_raw'])
        servo_4 = int(servo_message['servo4_raw'])

        print("Date: ", date)
        print("Latitude: ", latitude)
        print("Longitude: ", longitude)
        print("Roll: %f [rad]" % roll)
        print("Pitch: %f [rad]" % pitch)
        print("Yaw: %f [rad]" % yaw)
        print("Servo 1: ", servo_1)
        print("Servo 2: ", servo_2)
        print("Servo 3: ", servo_3)
        print("Servo 4: ", servo_4)
        print("================================")
        csvWriter.writerow([date, latitude, longitude, roll, pitch, yaw, servo_1, servo_2, servo_3, servo_4])

    except KeyboardInterrupt as e:
        print(e)
        exit(0)
        file.close()