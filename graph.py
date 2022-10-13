"""
This program is used from the command line where you input a file name after
calling the program. It will then ask for a y coordinate to read a line of
pixels from. Afterwards, it will print a graph, using the intensity of the RGB
value of each pixel.
"""
from PIL import Image
import sys
import numpy as np
import matplotlib.pyplot as plot

# im = 'C:/Users/Veltrace/Documents/USU/PHYS 3870/lab3/data/pic#.jpg'
im = Image.open(sys.argv[1])
if len(sys.argv) < 1:
    print("to use progam:\n"
          "graph.py [IMAGENAME.FILETYPE]\n"
          "Be sure to put in the appropriate path for the file\n")
    sys.exit(1)

col, row = im.size

pixels = im.load()

ytest = 1331 # used y value
# ytest = int(input("enter y coordinate to take [int only]: "))
xlist = []
R = []

for y in range(row):
    if y == ytest:
        for x in range(col):
            r, g, b = pixels[x, y]
            total = r + g + b
            xlist.append(total)
            R.append(x)

xaxis = np.array(xlist)
yaxis = np.array(R)

plot.xlabel('Distance, pixels')
plot.ylabel('Intensity (based on adding the RGB value of each pixel)')
plot.title('Experimental Data')

plot.plot(yaxis, xaxis)

plot.show()
