from math import *
# converting angles and finding sines

Angle = eval (input ('Enter the measure of the angle: '))

Angle_degree = degrees(Angle)

Angle_sine = sin(Angle_degree)

print('The sine of ',round(Angle_degree,3), ' = ',Angle_sine)
print('The angle entered in degrees = ',round(Angle_degree,3))