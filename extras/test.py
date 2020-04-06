# Importing libraries and modules
import cv2
import numpy as np
import pandas as pd

import math
import os

from shapes import contours, color, shape, centroid

"""
For the purpose of simplicity, we will be following HSV color format, rather than LAB color format for now.

TODO:
* Read the video frame
* Crop the image frame
* Grayscale the image
* blur the image to remove the noise
* Color Thresholding for binary image
* Contour Detection
* Find the largest contour as contour heirarchy
* For the largest contour(which is the path), find their moment and centroids.

"""
------------------------------------------------------------------------------
# Load all the seedling image in their variables

#assorted
#carnation
#gerber
#hibiscusred
#hibiscusyellow
#hydrangeablue
#hydrangeayellow
#lilac
#lily
#marigold
#morningglory
#orchid
#poinsettia
#rosesred
#rosesyellow
#sunflower
#tulipblue
#tulipred
------------------------------------------------------------------------------
"""
Inputing data from csv file as pandas dataframe.

csv_input stores the seedlings configuration file as pandas dataframe.
And assign each color marker their configured seedling name.
"""
#csv_input = pd.read_csv('./input.csv')
#print(csv_input)

# Assigning all the variable their desired seedling configuration
#red_square
#red_circle 
#red_triangle

#blue_square
#blue_circle
#blue_triangle

#green_square
#green_circle
#green_triangle 
------------------------------------------------------------------------------

# Reading test image
test_image = cv2.imread("./TestImages/1.jpg")

# Convert the image

