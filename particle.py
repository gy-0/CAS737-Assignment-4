import numpy as np

class Particle:
	def __init__(self, x, y):
		self.pos = np.array([x, y])
		self.mass = 1
		self.force = np.array([0, 0])
		self.velocity = 0
		self.acc = 0

	def update(self):
		pass #TODO 5: update particle's velocity & position

	def add_force(self, f):
		self.force = self.force + f