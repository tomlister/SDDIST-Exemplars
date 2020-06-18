class world:
	def __init__(self):
		self.map = []
		self.mapraw = []
		self.spaces = {}
		self.max_x = 0
		self.max_y = 0
	def get(self, x, y):
		return self.map[y][x]
		
class spaces:
	def __init__(self):
		self.data = {}
	def __getitem__(self, name):
		return self.data[name]
	def addspace(self, space):
		self.data[space.name] = space

class space:
	def __init__(self):
		self.name = ""
		self.enter = None
		self.options = []

class xy:
	def __init__(self):
		self.x = 0
		self.y = 0
	def set(self, x, y):
		self.x = x
		self.y = y
		

def loadmap(filename):
	#space format
	#id - (0x80 to 0xff) string-id - ASCII

	#map format
	#magic - CYOA - 0x43594f41
	#spaces: space - delimeted by 0x1e
	#mapdatamagic - MD - 0x4d44
	#mapdata: spaceid - line delimeted by 0x0d
	#end - 0x04
	tworld = world()
	file = open(filename, "rb").read()
	if file[:4] == b'CYOA':
		spaceid = 0x00
		stringid = ""
		mapstart = 0
		for i in range(4, len(file)):
			if file[i] == 0x1e:
				tworld.spaces[spaceid] = stringid
				spaceid = 0x00
				stringid = ""
			else:
				if spaceid == 0x00:
					if file[i:i+2] == b'MD':
						mapstart = i + 2
						break
					else:
						spaceid = file[i]
				else:
					stringid += chr(file[i])
		ml = []
		rml = []
		for i in range(mapstart, len(file)):
			if file[i] == 0x0d:
				tworld.map.append(ml)
				tworld.mapraw.append(rml)
				ml = []
				rml = []
			else:
				if file[i] == 0x04:
						break
				else:
					ml.append(tworld.spaces[file[i]])
					rml.append(file[i])
	tworld.max_x = len(tworld.map[0])
	tworld.max_y = len(tworld.map)
	return tworld


