"""
	Main class for PyPendulum. Uses agent.py to attempt an optimal solution to
	the inverted pendulum problem.
"""

from pendulum import *
from agent import *

def calculateReward():
	return 1

# Time between updates
dt = 0.1

pen = Pendulum()
agent = Agent()
while(pen.isHorizontal() == False):
	action = agent.getAction(pen.x, pen.v)
	pen.update(0.1, action)
	agent.notify(calculateReward())