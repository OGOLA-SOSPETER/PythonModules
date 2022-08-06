from math import *
#printing sine and cosine of angles

for p in range(0,360,15):
    Angle = p
    Angle_sine = sin(Angle)
    Angle_Cosine = cos(Angle)

    print(Angle,' -'*3,' ',round(Angle_sine,4), ' ',round(Angle_Cosine,4))