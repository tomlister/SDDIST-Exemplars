import spatial
import time
import globalv

class player:
	def __init__(self):
		self.alive = True
		self.inventory = []
		self.position = spatial.xy()
		self.traveldelay = 5
	def moveforward(self):
		if self.position.y < globalv.MAX_Y -1:
			self.position.set(self.position.x, self.position.y+1)
	def movebackward(self):
		if self.position.y > 0:
			self.position.set(self.position.x, self.position.y-1)
	def moveleft(self):
		if self.position.x > 0:
			self.position.set(self.position.x-1, self.position.y)
	def moveright(self):
		if self.position.x < globalv.MAX_X -1:
			self.position.set(self.position.x+1, self.position.y)

	def move(self, movetext):
		self.delay()
		if movetext == 'forward':
			self.moveforward()
		elif movetext == 'backward':
			self.movebackward()
		elif movetext == 'left':
			self.moveleft()
		elif movetext == 'right':
			self.moveright()
	def use(self, name):
		found = False
		for i in range(0, len(self.inventory)):
			if self.inventory[i] == name:
				found == True
				self.inventory.remove(name)
		return found
	def lowerdelay(self):
		self.traveldelay -= 1
	def delay(self):
		print('Travelling...')
		time.sleep(self.traveldelay)
	def kill(self):
		self.alive = False
	def give(self, name):
		self.inventory.append(name)




