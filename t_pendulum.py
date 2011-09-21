from pendulum import *
import unittest

class PendulumTest(unittest.TestCase):
	"""
		This class verifies that pendulum.Pendulum is executing properly.
	"""

	def setUp(self):
		pass
		
	def testInitPosition(self):
		"""When a Pendulum is created the x value should fall within the range -5*math.pi/180 and 5*math.pi/180."""
		for i in range(0, 100):
			p = Pendulum()
			self.assertTrue(-5*math.pi/180 <= p.x and p.x <= 5*math.pi/180)
			
	def testInitVelocity(self):
		"""When a Pendulum is created the v value should fall within the range -5*math.pi/180 and 5*math.pi/180."""
		for i in range(0, 100):
			p = Pendulum()
			self.assertTrue(-5*math.pi/180 <= p.v and p.v <= 5*math.pi/180)

	def testIsHorizontal(self):
		"""The method isHorizontal should return true if the pendulum is horizontal."""
		p = Pendulum()
		p.x = math.pi/2
		self.assertTrue(p.isHorizontal())
		p.x = -math.pi/2
		self.assertTrue(p.isHorizontal())

	def testIsNotHorizontal(self):
		"""The method isHorizontal should returen false if the pendulum is not horizontal."""
		p = Pendulum()
		for i in range(0, 100):
			p.x = uniform(-math.pi/2 - 2*epsilon, math.pi/2 + 2*epsilon)
			self.assertFalse(p.isHorizontal())
			
	def testUpdate(self):
		pass
			
	def testUpdateWhenHorizontal(self):
		"""The update() method should set the velocity to 0 when the pendulum is horizontal."""
		p = Pendulum()
		p.x = math.pi/2
		p.update(0.1, 50)
		self.assertEqual(p.v, 0)
		p.v = 1
		p.x = -math.pi/2
		p.update(0.1, -50)

if __name__ == '__main__':
    unittest.main()