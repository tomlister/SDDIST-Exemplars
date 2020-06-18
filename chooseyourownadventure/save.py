import pickle

def savestate(filename, space_data, world_data, player):
	save = {"space_d": space_data, "world_d": world_data, "player_d": player}
	savedata = pickle.dumps(save)
	f = open(filename, "wb")
	f.write(savedata)