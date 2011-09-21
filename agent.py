"""
    LSPI-Learning Agent for use in PyPendulum.
"""

from random import *

class Agent:
	def __init__(self):
		pass
		
	def getAction(self, x, v):
		return choice([-50, 50]) # Right now just return a random choice
	 
	def notify(self, reward):
		pass # Don't give a crap.
		