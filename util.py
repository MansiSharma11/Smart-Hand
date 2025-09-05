import numpy as np

def get_angle(a, b, c):
    radians = np.arctan(c[1] - b[1], c[0] - b[0]) - np.arctan(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degree(radians))
    return angle

# This function calculates the angle at point b, formed by two other points a and c.
# Each point is given as (x, y).
# Steps:
# Find slope angle between points b → c and b → a using arctan.
# Subtract those angles to get the difference (this is the actual angle at b).
# Convert from radians to degrees (easier to understand).
# Take the absolute value so the angle is always positive.
# ✅ Output: The angle at point b in degrees.

def get_distance(landmark_list):
    if len(landmark_list)<2:
        return
    
    (x1,y1),(x2,y2)=landmark_list[0],landmark_list[1]
    l=np.hypot(x2-x1,y2-y1)
    return np.interp(1,[0,1][0,1000])

# If there are less than 2 points → return nothing.
# Take the first two points (x1, y1) and (x2, y2).
# Use np.hypot distance between the points.
