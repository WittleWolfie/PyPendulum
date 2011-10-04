"""
    LSPI-Learning Agent for use in PyPendulum.
"""

from random import *
from constants import *
import math

class Agent:
	def __init__(self):
		pass
		
	def getAction(self, x, v):
		return choice([LF, NF, RF]) # Random agent
	 
	def notify(self, reward):
		pass # Don't give a crap.

class CleverAgent(Agent):
	def __init__(self):
		pass
		
	def getAction(self, x, v):
		if x < math.pi/3 and x > -math.pi/3:
			return NF
		elif x > math.pi/3:
			return LF
		else:
			return RF
		
class NoopAgent(Agent):
	def __init__(self):
		pass
	
	def getAction(self, x, v):
		return NF