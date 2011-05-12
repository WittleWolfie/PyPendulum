"""
    Represents an inverted pendulum, keeping track of angle, angular velocity and angular acceleration.
    
    angular acceleration = (g*sin(x) - a*m*l*(v^2)*sin(2*x)/2 - a*cos(x)*u)/(4*l/3 - a*m*l*cos^2(x))
    x = angle
    v = angular velocity
    g = acceleration due to gravity
    m = mass of the pendulum
    M = mass of the cart
    l = length of the pendulum
    a = 1/(m+M)
"""

# Constants
g = 9.8
m = 2.0
M = 8.0
l = 0.5
a = 1.0/(m+M)