ansi_resources = {}
def load(name, filename):
	ansifile = open(filename)
	ansi_resources[name] = ansifile.read()
	ansifile.close()
	return name

def display(name):
	print(ansi_resources[name])