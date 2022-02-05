# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math


def calculate_distance(x1, y1, x2, y2):
    # Calculate the distance between the two circles.
    distance = math.sqrt((x1-x2)**2 + (y1 - y2)**2)
    return distance


def calculate_length(xa, ya, xb, yb):
    # calcualte the length of vector AB vector which is a vector between A and B points.
    length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
    return length


print('distance', calculate_distance(4, 4.25, 53, -5.35))

print('length', calculate_length(-36, 97, .34, .91))
