#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:21:00 2020

@author: qhu12
"""

import matplotlib.pyplot as plt
import numpy as np
# Declare constants of the slinky held in stationary state

Nf = 72 #number of free coils
Nc = 8 #number of non-free coils
mc = 2.5e-3 #mass of each coil (kg)
Lf = 1.00 #natural length of the slinky (m)
g = -9.80 #gravity acceleration, setting the downard direction as the positive direction (m/s^2)
kc = 76.6 #spring constant of the slinky (N/m)

DT = 3.342e-3 #collision time interval (s) the collision interval doesn't vary much, so I give it a constant value
N = Nf+Nc-1 #number of time intervals
T = N*DT #stimulation time duration (s)

V_initial = np.empty(N) 
a_com = np.empty(N)
V_final = np.empty(N)
time = np.empty(N)

#initial condition
V_initial[0] = 0 #the initial velocity of the first coil is released from rest (m/s)
a_com [0] = -1558 #the first acceleration of centre of mass (m/s^2)
V_final[0] = -6.56 #the final velocity of the first coil, right before the first coil collides with the second coil (m/s)

      
for j in range (0,N-1): #using loop to make an increment, j is the number of loops
    
    time[0] = 0 #initial time (s)
    
    time[1] = time[0]+DT #Euler's method for the increment of time
    
    time[j+1] = time[j]+DT #Euler's method
            
    a_com [0] = -1558 #initial acceleration (m/s^2)
    
    V_initial[0] = 0 #initial velocity (m/s)

    V_final[0] = -6.56 #first velocity right before the collision between the first and the second coil(m/s)
        
    a_com[j+1] = 2*(Nf+Nc)*g/(j+1)-g 
    #using euqation (7) in my paper to find the accelerations of the centre of mass (compressed coils)
                
    V_initial[j+1] = j/(j+1)*V_final[j] 
    #using equation (9) to find the velocities of top coils as it collapses with coils below it      
        
    V_final[j+1] = V_initial[j+1] + a_com[j+1]*DT 
    #using kinetics equation Vfinal = Vinitial + a*t
                
    j+=1 #each time after collision, the number of coils increased by 1

plt.figure(figsize=[21,9], dpi=50)

plt.plot(time, V_initial, color = "xkcd:blue")

plt.title('Velocity of Top Coil in Slinky vs. Time', fontsize = 36, weight = "bold", family = "Serif")

plt.xlabel('Time (s)',fontsize = 30, family="serif",labelpad =8 )

plt.ylabel('Velocity (m/s)', fontsize = 30, family="serif", labelpad =8)

plt.grid(True, axis = 'y', alpha = 0.5)

plt.plot()




