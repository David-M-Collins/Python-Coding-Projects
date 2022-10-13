"""
Call the function with an image file and it will display it to the screen
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

# image = 'C:/Users/Veltrace/Documents/USU/PHYS 3870/lab3/data/pic#.jpg'
image = sys.argv[1]
if len(sys.argv) < 1:
    print("to use progam:\n"
          "plot.py [IMAGENAME.FILETYPE]\n"
          "Be sure to put in the appropriate path for the file\n")
    sys.exit(1)
img = mpimg.imread(image)
imgplot = plt.imshow(img)
plt.show()
