# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 07:35:00 2018

@author: astraszab

Plot the Barnsley fern fractal
"""

from random import choices
from pylab import plot

NUMBER_OF_POINTS = 400000
STARTING_X = 0
STARTING_Y = 0
PROBABILITIES = (0.01, 0.85, 0.07, 0.07)
COEFFICIENTS = (
        (    0,     0,     0, 0.16, 0,    0),
        ( 0.85,  0.04, -0.04, 0.85, 0, 1.60),
        ( 0.20, -0.26,  0.23, 0.22, 0, 1.60),
        (-0.15,  0.28,  0.26, 0.24, 0, 0.44))

def next(x, y):
    # Generate the next point
    
    # Choose randomly a row from coefficients, depending on probabilities
    row = choices(COEFFICIENTS, weights=PROBABILITIES)[0]
    
    # Apply coefficients to calculate the next point coordinates
    a, b, c, d, e, f = row
    next_x = a * x + b * y + e
    next_y = c * x + d * y + f
    
    return next_x, next_y
    

# Initialize starting coordinates
x = STARTING_X
y = STARTING_Y

# Create lists of coordinates
xVals = []
yVals = []

# Generate points
for i in range(NUMBER_OF_POINTS):
    xVals.append(x)
    yVals.append(y)
    x, y = next(x, y)
    
# Plot all the points
plot(xVals, yVals, 'g,')