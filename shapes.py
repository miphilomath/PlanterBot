import cv2
import numpy as np
from matplotlib import pyplot as plt

from collections import OrderedDict
import math

def contours(image):
    # to find the contours of the image, image needs to be grayscale binary
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(image_gray)
    # Applying threshhold to convert in binary image
    ret, image_binary = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Applying contours
    image_contour, contours, heirarchy = cv2.findContours(image_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contour image in image_contour with black color
    image_contour = cv2.drawContours(image, contours, -1, (0, 0, 0), 3)
    return image_contour, contours

def centroid(contour):
    # Calculating moments to find centroid
    M = cv2.moments(contour)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    return cx, cy

def shape(object):
    """
    First we find the perimeter of the contour and using approxpolydp method,
    We detect the shape of the object.
    Shapes that needs to be checked for:
        - Triangle
        - Rhombus
        - Trapezium
        - Pentagon
        - Hexagon
        - Circle: approx_poly = 16 for epsilon(0.01)
    """
    shape = ""
    perimeter = cv2.arcLength(object, True)
    approx_poly = cv2.approxPolyDP(object, 0.01 * perimeter, True)
    print len(approx_poly)
    
    # Logic to check the shape of the object
    if len(approx_poly) == 3:
        shape = "Triangle"
    elif len(approx_poly) == 4:
        # The object can be any quadrilateral
        # Check for Trapezium and rhombus
        # Compute the bounding box of the contour and use
        # the bounding box to compute the aspect ratio
        # Rhombus have better aspect ratio than trapezium
        # Using Bounding Rectangle, later changed to rotated rectangle
        # Aspect ratio for Rhombus is 1.57...
        # Aspect ratio for Trapezium is 2.03...
        (x, y, w, h) = cv2.boundingRect(object)
        aspect_ratio = float(w) / h

        shape = "Rhombus" if aspect_ratio >= 1.5 and aspect_ratio <= 1.9 else "Trapezium"
        
    elif len(approx_poly) == 5:
        shape = "Pentagon"
    elif len(approx_poly) == 6:
        shape = "Hexagon"
    else:
        shape = "Circle"

    return shape

def color(image_hsv, object):
    """
    The function converts the image in HSV colorspace
    Can also solve this problem in RGB or BGR format :P
    Check each contour for each color and returns the color for that contour.
    Color checked are RED, BLUE and GREEN only.
    Input contour is in BGR colorspace, so convert it first.
    
    HSV Value with range (+-10)
       - Blue: [120,255,255]
       - Red: [0,255,255]
       - Green: [60,255,255]

    We take mean hsv value of object and compare with standard values of RED, BLUE, GREEN
    """

    # Creating mask for the object from image
    mask = np.zeros(image_hsv.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [object], -1, 255, -1)

    # Calculating color mean for the object
    color_mean = cv2.mean(image_hsv, mask=mask)[:3]
    
    # Find min distance of the mean hsv of object from the
    # HSV value of RED, BLUE, and GREEN
    # Using Euclidean distance, least distance is the color for object
    min_distance = (np.inf, None)

    # Logic to calculate the minimum distance from each color in colors_hsv
    for (iter, color) in enumerate(colors_hsv):
        # Euclidean distance calculation using list comprehension
        dis = math.sqrt(sum([(a - b) ** 2 for a, b in zip(color[0], color_mean)]))

        if dis < min_distance[0]:
            # Saving the min distance along with its iterator value
            min_distance = (dis, iter)
            
    return (color_names[min_distance[1]]) 
       
#def generate_output():

#def count_objects(contour_data):
#    return len(contour_data)


#def main():

if __name__ == "__main__":

    circle = cv2.imread('E:\\circle.png')
    hexagon = cv2.imread('E:\\hexagon.png')
    pentagon = cv2.imread('E:\\pentagon.png')
    rhombus = cv2.imread('E:\\rhombus.png')
    trapezium = cv2.imread('E:\\trapezium.png')
    triangle = cv2.imread('E:\\triangle.png')
    
    Sample1 = cv2.imread('E:\\Sample1.png')

    image = Sample1

    # Getting the contours of the image as a tuple of image_contour and contour_data
    image_contour, contour_data = contours(image)
    
    # Count the objects
    object_count = len(contour_data)

    # HSV image
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #------------------------To calculate Colors_hsv used by color() function------#

    # The dictionary of color with RGB format
    colors_dict = OrderedDict({
        "Red": (255, 0, 0),
        "Green": (0, 255, 0),
        "Blue": (0, 0, 255)})
    color_names = []

    global colors_hsv
    
    # Creating empty array for HSV color codes of RGB colors
    colors_hsv = np.zeros((len(colors_dict), 1, 3), dtype="uint8")

    for (iter, (col_name, rgb_code)) in enumerate(colors_dict.items()):
        colors_hsv[iter] = rgb_code
        color_names.append(col_name)
    colors_hsv = cv2.cvtColor(colors_hsv, cv2.COLOR_RGB2HSV)
    #------------------------------------------------------------------------------#
    
    for object in contour_data:
        cen_x, cen_y = centroid(object)
        object_color = color(image_hsv, object)
        object_shape = shape(object)
        
        # Beware, send the contour image in BGR colorspace for it to word
        # object_color = color(object)
        print("Centroid of the object is {0},{1}".format(cen_x, cen_y))
        print("Color of this object is {0}".format(object_color))
        print("The Shape of the object is {0}".format(object_shape))

        # To write the details of the image on it
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(image, object_color, (cen_x, cen_y), font, 4, (0, 0, 0), 2, cv2.LINE_AA)
        #cv2.putText(image, object_shape, (cen_x, cen_y), font, 4, (0, 0, 0), 2, cv2.LINE_AA)
        #cv2.putText(image, "{0}, {1}".format(cen_x, cen_y), (cen_x, cen_y), font, 4, (0, 0, 0), 2, cv2.LINE_AA)
        

    print("The Number of objects in this image is : {0}".format(object_count))

