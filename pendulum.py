"""
    Represents an inverted pendulum, keeping track of angle, angular velocity and angular acceleration.
    
    angular acceleration = (g*sin(x) - a*m*l*(v^2)*sin(2*x)/2 - a*cos(x)*u)/(4*l/3 - a*m*l*cos^2(x))
    x = angle (rad)
    v = angular velocity (rad/s)
    g = acceleration due to gravity (m/s^2)
    m = mass of the pendulum (kg)
    M = mass of the cart
    l = length of the pendulum (m)
    u = force applied (N)
    a = 1/(m+M)
"""

from random import *
import math

# Constants
g = 9.8
m = 2.0
M = 8.0
l = 0.5
a = 1.0/(m+M)
epsilon = 0.000001
import pdb

class Pendulum:
    # Initially the pendulum is set to a slightly unstable state near (x,v) = (0, 0)
    def __init__(self):
        self.x = uniform(-5*math.pi/180, 5*math.pi/180)
        self.v = uniform(-5*math.pi/180, 5*math.pi/180)
        
    # Updates the state of the pendulum
    # IMPORTANT NOTE: This is an approximate update step, with error proportional to the size of dx and
    # the angular velocity and acceleration.
    def update(self, dt, u):
        self.x += self.v*dt
        
        # Check if we have hit 90 degrees, if so we are stable
        if self.x - math.pi/2 >= -epsilon:
            self.x = math.pi/2
            self.v = 0
        elif self.x + math.pi/2 <= epsilon:
            self.x = -math.pi/2
            self.v = 0
        else:
            accel = (g*math.sin(self.x) - a*m*l*self.v*self.v*math.sin(2*self.x)/2 - a*math.cos(self.x)*u)
            accel = accel/(4*l/3 - a*m*l*math.pow(math.cos(self.x), 2))
            self.v += accel*dt
            
pdb.set_trace()