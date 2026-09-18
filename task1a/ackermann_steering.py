'''
*****************************************************************************************
*
*  ===============================================
*     Niti Vahan (NV) Theme of eYRC 2026-27
*  ===============================================
*
*  This script is intended for implementation of Task 1A of Niti Vahan (NV) Theme.
*
*  Filename:         ackermann_steering.py
*  Created:          2026
*  Last Modified:
*  Author:           e-Yantra Team
*
*  You are ONLY allowed to write your code inside the block marked
*  "ADD YOUR IMPLEMENTATION HERE". Do not change anything outside it - the
*  evaluation script relies on the rest of this file staying as it is.
*
*****************************************************************************************
'''

# Team ID:          < Team-ID >
# Author List:      < Names of the team members who worked on this file, comma separated >
# Filename:         ackermann_steering.py
# Functions:        ackermann_wheel_angles
# Global variables: < List any global variables you add, "None" if you add none >


####################### IMPORT MODULES #######################
import math
import numpy as np
##############################################################


#################### VEHICLE CONSTANTS #######################
WHEELBASE = 0.120           # L: distance between front and rear axle centrelines
TRACK_WIDTH = 0.110         # W: distance between left and right wheel centre
WHEEL_OFFSET = 0.0275       # O: distance between kingpin axis and wheel centre.
##############################################################


##############################################################
############### ADD YOUR IMPLEMENTATION HERE #################
##############################################################


def ackermann_wheel_angles(delta):
    '''
    Purpose:
    ---
    Convert a single virtual steering angle into the two real front-wheel
    angles, per the Ackermann geometry.

    Input Arguments:
    ---
    `delta` :   [ float ]
        Steering angle of the virtual centred front wheel, in radians.

    Returns:
    ---
    `left_angle`  : [ float ]
    `right_angle` : [ float ]
        The two real front-wheel steering angles, in radians, using the
        same sign convention as delta.

    REMEMBER:
    ---
    WHEEL_OFFSET changes the effective half-track width inside each wheel's triangle.
    '''

    # If the vehicle is going straight
    if delta == 0:
        return 0.0, 0.0

    # Vehicle dimensions
    L = WHEELBASE
    half_track = (TRACK_WIDTH / 2) - WHEEL_OFFSET

    # Calculate turning radius
    turn_radius = radius_from_angle(delta)

    # Calculate inner and outer wheel angles
    inner_angle = math.atan(L / (turn_radius - half_track))
    outer_angle = math.atan(L / (turn_radius + half_track))

    # Positive delta = left turn
    # Negative delta = right turn
    if delta > 0:
        left_angle = inner_angle
        right_angle = outer_angle
    else:
        left_angle = -outer_angle
        right_angle = -inner_angle

    return left_angle, right_angle


# ---- helpers, still inside the implementation block ----

def radius_from_angle(delta):
    '''
    Calculate the turning radius from the virtual steering angle.
    '''

    radius = abs(WHEELBASE / math.tan(delta))

    return radius




##############################################################
################ END OF YOUR IMPLEMENTATION ##################
##############################################################


#################### DO NOT EDIT BELOW THIS LINE ####################

if __name__ == "__main__":

    test_angles = np.arange(-0.35, 0.35, 0.05)

    for d in test_angles:
        left, right = ackermann_wheel_angles(d)
        print(f"delta={d}  ->  left={left}, right={right}")
