import math
class vector(object):
	"""docstring for vector"""
	def __init__(self, x=0.0,y=0.0):
		self.x = x
		self.y = y


	@staticmethod
	def from_points(p1,p2):
		return vector(p1.x-p2.x,p1.y-p2.y)
	
	def __add__(self,ob):
		ob3 = vector()
		ob3.x = self.x+ob.x
		ob3.y = self.y+ob.y
		return ob3
	
	def __sub__(self,ob):
		ob3 = vector()
		ob3.x = self.x - ob.x
		ob3.y = self.y - ob.y
		return ob3
	
	def __mul__(self,scalar):
		ob3 = vector()
		ob3.x = self.x * scalar
		ob3.y = self.y * scalar
		return ob3
	def directionmult(self,dir_vec):
		self.x = self.x * dir_vec.x
		self.y = self.y * dir_vec.y
	def print(self):
		ret = str(self.x) + "i + " + str(self.y) + "j"
		return ret
	
	def magnitude(self):
		mag = math.sqrt(self.x**2 + self.y**2)
		return mag
	
	def normalize(self):
		if self.x !=0 and self.y != 0:
			mag = self.magnitude()
			self.x = self.x / mag
			self.y = self.y / mag
		else :
			self.x = 0
			self.y = 0
	def tupleit(self):
		return (self.x,self.y)
			
	def ifequal(self,ob):
		if self.x == ob.x:
			if self.y == ob.y:
				return True
		else :
			return False		