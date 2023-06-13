'''
function_compute_def.py

Functions to compute the vertical and the horizontal deformation created by a Geertsma disk

Equations 6 and 7 from Geertsma 1973
'''

import numpy as np

##################
## Base coordinate

def cart2pol(x1, x2):
    theta = np.arctan2(x2, x1)
    r = np.hypot(x2, x1)
    return theta, r

def pol2cart(theta, r):
    x1 = r * np.cos(theta)
    x2 = r * np.sin(theta)
    return x1, x2

################
## Forward model



def nucleus_u_cartesian(x, y, z, mogi, dh, nu, dl2, grid_degree):
    pi = np.pi
    # Earth radius [m]
    earth_rad = 6371000
    # earth circumference
    earth_cir = 2 * pi * earth_rad
    # Distance between the source and the grid point
    x = x - mogi[0]
    y = y - mogi[1]
    z = z - mogi[2] 
    if (grid_degree == 1):
        x = x * (earth_cir / 360)  # [m] ! circumference
        y = y * (earth_cir / 360)  # [m]
        
    # Distance nucleus-observation    
    R = np.sqrt(x**2 + y**2 + z**2)
    
    ## Compute subsidence
    #C = Cm * ((1 - nu) / np.pi) * dP * V
    #C = ((1 - nu) / np.pi) * dh * V
    C = ((1 - nu) / np.pi) * dh * dl2
    ux = C * x / (R ** 3)
    uy = C * y / (R ** 3)
    uz = - C * mogi[2] / (R ** 3)
    
    u = np.array([ux, uy, uz]) # verification for uz: same in both function (good)

    return u



