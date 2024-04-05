import numpy as np
class Spring:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.rest_length = np.linalg.norm(p1.pos - p2.pos)

	def apply_force(self):
		pass #TODO 4: compute spring force
