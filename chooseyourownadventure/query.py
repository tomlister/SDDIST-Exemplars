def parse_movement(q):
	verbs = ["move", "go", "travel", "walk"]
	directions = {"left":"left", "right":"right", "forward":"forward", "forwards":"forward", "back":"backward", "backward":"backward", "backwards":"backward"}
	qs = q.lower().split(" ")
	if qs[0] in verbs:
		if qs[1] in directions:
			return False, directions[qs[1]]
		else:
			return True, "I don't know what "+qs[1]+" is."
	else:
		return True, "I don't know what "+qs[0]+" is."