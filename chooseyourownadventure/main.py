import spatial
import content.field
import content.river
import content.fieldb
import content.bear
import content.bridge
import content.fieldc
import content.forest
import player
import save
import globalv

spaces_data = spatial.spaces()
spaces_data.addspace(content.field.init())
spaces_data.addspace(content.river.init())
spaces_data.addspace(content.fieldb.init())
spaces_data.addspace(content.bear.init())
spaces_data.addspace(content.bridge.init())
spaces_data.addspace(content.fieldc.init())
spaces_data.addspace(content.forest.init())
#read from a file fufilling the criteria "Reads game data in from a file."
world_data = spatial.loadmap("content/main.map")
#cheeky little world globals
globalv.MAX_X = world_data.max_x
globalv.MAX_Y = world_data.max_y
#player
player_0 = player.player()
#game loop
while True:
	if player_0.alive == True:
		spaces_data[world_data.get(player_0.position.x, player_0.position.y)].enter(player_0, spaces_data[world_data.get(player_0.position.x, player_0.position.y)])
	else:
		break
#saving to a file fufilling the criteria of "Ability to save the game."
save.savestate("0.save", spaces_data, world_data, player_0)
