"""
    Main class for PyPendulum. Uses agent.py to attempt an optimal solution to
    the inverted pendulum problem.
"""

from pendulum import *
from agent import *

# Time between updates
dt = 0.1

pen = Pendulum()
agent = Agent()
while(!pen.isHorizontal()):
    action = agent.getAction(pen.x, pen.v)
    agent.notify(calculateReward())