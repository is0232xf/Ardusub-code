import math
import numpy as np

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


#  // rotate vector from vehicle's perspective to North-East frame
#  void Copter::rotate_body_frame_to_NE(float &x, float &y)
#  {
#      float ne_x = x*ahrs.cos_yaw() - y*ahrs.sin_yaw();
#      float ne_y = x*ahrs.sin_yaw() + y*ahrs.cos_yaw();
#      x = ne_x;
#      y = ne_y;
#  }

def rotate_body_frame_to_NE(x, y, w):
    ne_x = round(x * math.cos(math.radians(w)) - y * math.sin(math.radians(w)),6)
    ne_y = round(x * math.sin(math.radians(w)) + y * math.cos(math.radians(w)),6)

    d = math.sqrt(math.pow(ne_x, 2) + math.pow(ne_y, 2))

    return ne_x, ne_y, d

# w1 = 0

# x = 5
# y = 5
# l1 = 0
# l2 = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# theta = np.radians(0)

# c, s = np.cos(theta), np.sin(theta)

# R1 = np.array(
#     (
#     (c,-s), 
#     (s, c)
#     )
#     )

# print(R1) 

# L1 = np.array(
#     (
#         (l1), (0)
#     )
# )
# print(L1) 

# R = R1*L1

# print(R)

# theta2 = np.radians(45)

# c2, s2 = np.cos(theta2), np.sin(theta2)

# R2 = np.array(
#     (
#     (c2,-s2), 
#     (s2, c2)
#     )
#     )

# print(R2) 
# L2 = np.array(
#     (
#         (l2), (0)
#     )
# )
# print(L2) 


# R = R1*L1 + R1*R2*L2

# print("Result??")
# print(R)

print("0")
print(np.around(rotate((0,0), (5,5), math.radians(0)),6))
print(rotate_body_frame_to_NE(5,5,0))

print("45")
print(np.around(rotate((0,0), (5,5), math.radians(45)),6))
print(rotate_body_frame_to_NE(5,5,45))

print("90")
print(np.around(rotate((0,0), (5,5), math.radians(90)),6))
print(rotate_body_frame_to_NE(5,5,90))

print("135")
print(np.around(rotate((0,0), (5,5), math.radians(135)),6))
print(rotate_body_frame_to_NE(5,5,135))

print("180")
print(np.around(rotate((0,0), (5,5), math.radians(180)),6))
print(rotate_body_frame_to_NE(5,5,180))

print("225")
print(np.around(rotate((0,0), (5,5), math.radians(225)),6))
print(rotate_body_frame_to_NE(5,5,225))


# wi = 0
# x = 5
# y = 5

# d = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
# wr = (math.atan2(x,y) * 180) /  math.pi

# w = wi + wr

# print d
# print wr
# print w

# #print math.radians(90)
# #print math.cos(math.radians(90))

# y = round(math.cos(math.radians(w)) * d, 6)
# x = round(math.sin(math.radians(w)) * d, 6)

# print "x ", x
# print "y ", y
