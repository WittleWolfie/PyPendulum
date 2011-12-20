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

num_trials = 10000

# Track time alive
random_agent_life = 0
clever_agent_life = 0
noop_agent_life = 0

for i in range(0, num_trials):
	# Random agent, huzzah!
	pen = Pendulum()
	agent = Agent()
	samples = list()
	while(pen.isHorizontal() == False):
		# Track samples for the random agent
		sample = list()
		sample.append((pen.x, pen.v))

		# Get action and update
		action = agent.getAction(pen.x, pen.v)
		pen.update(0.1, action)
		reward = calculateReward()
		agent.notify(reward)

		# Update the sample
		sample.append(action)
		sample.append(reward)
		sample.append((pen.x, pen.v))
		samples.append(sample)

		random_agent_life += 1
		
	# Clever agent, hoorah!
	pen = Pendulum()
	agent = CleverAgent()
	while(pen.isHorizontal() == False):
		action = agent.getAction(pen.x, pen.v)
		pen.update(0.1, action)
		agent.notify(calculateReward())
		clever_agent_life += 1
		
	# Noop agent, hooplah!
	pen = Pendulum()
	agent = NoopAgent()
	while(pen.isHorizontal() == False):
		sample =
		action = agent.getAction(pen.x, pen.v)
		pen.update(0.1, action)
		agent.notify(calculateReward())
		noop_agent_life += 1
	
print "\nSummary:\n"
print "Random Agent: %f" % ((random_agent_life*0.1)/num_trials)
print "Clever Agent: %f" % ((clever_agent_life*0.1)/num_trials)
print "No-Op Agent: %f" % ((noop_agent_life*0.1)/num_trials)