"""
The script uses two given points and the distance formula to calculate
the distance between the two points on the image in pixels. To get the
real units, divide the distance by the image's width, resulting in a
number between 0 and 1, and multiply that number by the width of the
image in reality – that is, the span of the rightmost and leftmost
pixels of the image in real life, like 30 centimeters or 2.3 miles.
"""

import numpy as np
from PIL import Image
from math import sqrt
import sys

# image = 'C:/Users/Veltrace/Documents/USU/PHYS 3870/lab3/data/pic#.jpg'
image = sys.argv[1]
if len(sys.argv) < 1:
    print("to use progam:\n"
          "IM.py [IMAGENAME.FILETYPE]\n"
          "Be sure to put in the appropriate path for the file\n")
    sys.exit(1)

img = Image.open(image)
pixels = np.array(img)
img.close()

width, height, channels = pixels.shape
w, h = img.size

print(w, h)

actual_width = 80.5 # width of the photos
actual_units = "mm"
y_value = 1331 # our constant y value

x1 = int(input("x1 = "))
y1 = y_value
x2 = int(input("x2 = "))
y2 = y1

pixel_distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

actual_distance = (pixel_distance / width) * actual_width

print(f"The distance between the two points is about {actual_distance:.3f} {actual_units}")
