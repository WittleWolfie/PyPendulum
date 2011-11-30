"""
    LSPI-Learning Agent for use in PyPendulum.
"""

from random import *
from constants import *
from numpy import *
import math

class Agent:
	def __init__(self):
		pass
		
	def getAction(self, x, v):
		return choice([L, N, R]) # Random agent
	 
	def notify(self, reward):
		pass # Don't give a crap.

class CleverAgent(Agent):
	def __init__(self):
		pass
		
	def getAction(self, x, v):
		if x < math.pi/6 and x > -math.pi/6:
			return N
		elif x > math.pi/6:
			return L
		else:
			return R
		
class NoopAgent(Agent):
	def __init__(self):
		pass
	
	def getAction(self, x, v):
		return N

class LSPIAgent(Agent):
	# A sample of data collected from the target environment
	# must be passed to the constructor.
	def __init__(self, sample, discount=0.9):
		self.discount = discount

	# State should be the tuple (x, v) and action should be RF, NF, or LF
	def basis_function(state, action):
		sigma2 = 1
		phi = zeros(10, 3)
		
		if state[0] - math.pi/2 >= -epsilon or state[0] + math.pi/2 <= epsilon
			return phi
		
		
