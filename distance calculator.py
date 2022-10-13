from math import *

s = [34.899, 19.726, 35.245, 20.737, 36.470, 21.137,
     36.816, 21.376, 38.600, 22.255, 38.946, 23.053,
     41.688, 23.639, 42.726, 24.863, 45.308, 25.689]  # distances measured
# s = [34.539, 19.661, 34.874, 20.661, 36.059, 21.057,
#      36.393, 21.293, 38.113, 22.161, 38.446, 22.949,
#      41.075, 23.527, 42.066, 24.733, 44.521, 25.545]  # 'real' length
m = ["4.75 outer", "4.75 inner", "4.50 outer", "4.50 inner", "4.25 outer", "4.25 inner",
     "4.00 outer", "4.00 inner", "3.75 outer", "3.75 inner", "3.50 outer", "3.50 inner",
     "3.25 outer", "3.25 inner", "3.00 outer", "3.00 inner", "2.75 outer", "2.75 inner"]  # voltage and rings
v = [4.75, 4.75, 4.50, 4.50, 4.25, 4.25,
     4.00, 4.00, 3.75, 3.75, 3.50, 3.50,
     3.25, 3.25, 3.00, 3.00, 2.75, 2.75]  # voltages for measurements
diam = 140  # length between the graphite and the detection plate
R = 66  # curvature of the sphere or it's given radius

# print("Supposed corrected length from picture arc length to 'real' length")
# for i in range(0, 18):
#     theta = ((360*s[i])/(pi*diam))/2
#     thetax = radians(theta)
#     x = diam*sin(thetax)
#
#     print(m[i] + " " + str(round(x, 3)) + " mm")
#     # print(str(round(x, 3)) + ", ")

print("\nCarbon atom spacings found from ring measurements in nm:")

for i in range(0, 18):
    a = s[i] / 2  # half the measured distance
    r = R*sin(a/R)  # true radius of the circle
    thetas = atan(r/(diam - R + sqrt(R**2 - r**2)))  # theta between carbon filament and screen
    d = 2 * diam * 1.23 / (2*r * (v[i] * 1000)**(1/2))

    print(m[i] + " " + str(round(d, 3)) + " nm")
