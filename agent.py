"""
    LSPI-Learning Agent for use in PyPendulum.
"""

from random import *
import math

class Agent:
	def __init__(self):
		pass
		
	def getAction(self, x, v):
		return choice([-50, 0, 50]) # Right now just return a random choice
	 
	def notify(self, reward):
		pass # Don't give a crap.

class CleverAgent(Agent):
	def __init__(self):
		pass
		
	def getAction(self, x, v):
		if x < math.pi/3 and x > -math.pi/3:
			return 0
		elif x > math.pi/3:
			return -50
		else:
			return 50
		
class NoopAgent(Agent):
	def __init__(self):
		pass
	
	def getAction(self, x, v):
		return 0