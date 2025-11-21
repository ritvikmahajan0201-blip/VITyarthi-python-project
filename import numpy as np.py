#WAP for projectile motion
#plot the trajectory
#show diagramatically that at theta = 45 range will be maximum

#need input for theta and initial velocity from user
# then calculate the height AND range 
import numpy as np
import matplotlib.pyplot as plt
theta = int(input("Please enter the value of theta: "))
initial_velocity = int(input("Enter the value of initial velocity(u): "))
max_time = int(input("Enter the maximum time: "))
#time
time = np.linspace(0,max_time,100)
#xcomponent
x = []
x = initial_velocity*(np.deg2rad(np.cos(theta)))*time 

#WAP to evaluate the circular motion
#a) Patj trajectory
#b) Phase diff between x,y


