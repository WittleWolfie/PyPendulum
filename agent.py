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
		return choice([LF, NF, RF]) # Random agent
	 
	def notify(self, reward):
		pass # Don't give a crap.

class CleverAgent(Agent):
	def __init__(self):
		pass
		
	def getAction(self, x, v):
		if x < math.pi/6 and x > -math.pi/6:
			return NF
		elif x > math.pi/6:
			return LF
		else:
			return RF
		
class NoopAgent(Agent):
	def __init__(self):
		pass
	
	def getAction(self, x, v):
		return NF

class LSPIAgent(Agent):
	num_actions = 3
	basis_size = 10

	# A sample of data collected from the target environment
	# must be passed to the constructor.
	# Each sample should be a tuple (s,a,r,s')
	def __init__(self, sample, discount=0.9):
		self.discount = discount
		self.w = zeros(basis_size*num_actions)
		policy = self.lstdq(sample)

		# Loop until our policy converges
		while diff(self.w, policy) < epsilon:
			self.w = policy
			policy = self.lstdq(sample)

		self.w = policy

	# For LSPI the policy is already computed. Just find the maximum value action.
	def getAction(self, x, v):
		action = max = -9999
		for a in (RF, NF, LF):
			params = basis_function((x,v), a)
			q = dot(params, self.w)
			if q > max:
				action = a
				max = q

		return action

	# Performs LSTDQ-OPT on the sample. See the paper for more info.
	def lstdq(self, sample):
		B = eye(basis_size*num_actions)
		b = zeros(basis_size*num_actions)
		for s in sample: # s = (s, a, r, s')
			# First get the basis functions
			phi = basis_function(s[0], s[1])
			next_action = self.getAction(s[3][0], s[3][1])
			phi_prime = basis_function(s[3], next_action)

			# break the calculation into smaller parts
			temp = phi - self.discount*phi_prime
			num = dot(dot(B, phi.T), dot(temp, B))
			denom = 1 + dot(dot(temp,B), phi.T)
			B = B - num/denom

			# Update values
			b = b + phi*s[2]

		return dot(B,b)

	# Computes the difference between the magnitude of two vectors.
	def diff(a, b):
		mag_a = mag_b = 0
		for x in a:
			mag_a += x*x
		for x in b:
			mag_b += x*x
		mag_a = math.sqrt(mag_a)
		mag_b = math.sqrt(mag_b)

		return math.abs(a - b)

	# State should be the tuple (x, v) and action should be RF, NF, or LF
	def basis_function(state, action):
		sigma2 = 1
		phi = zeros((1, basis_size*num_actions))
		
		# If we're horizontal then the basis function is all 0s.
		if state[0] - math.pi/2 >= -epsilon or state[0] + math.pi/2 <= epsilon:
			return phi
		
		# Now populate the basis function for this state action pair
		# Note that each entry except for the first is a gaussian.
		i = basis_size * (action - 1)
		phi[i] = 1.0
		i += 1
		for x in (-math.pi/4.0, 0.0, math.pi/4.0):
			for y in (-1, 0, 1):
				dist = (state[0] - x)(state[0] - x) + (state[1] - y)(state[1] - y)
				phi[i] = math.exp(-dist/(2*sigma2))
				i += 1
		
		return phi
