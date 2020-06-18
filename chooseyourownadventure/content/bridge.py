import spatial
import art
import player
import query

def unlock(player_obj, space_obj):
	if 'unlocked' not in space_obj.options:
		if 'key' in player_obj.inventory:
			print("You open the gate.")
			space_obj.options.append('unlocked')
			player_obj.use('key')
		else:
			print("You don't have a key to unlock the gate.")
	else:
		print('The gate is already unlocked.')

def jump(player_obj):
	print('')
	art.display("blood")
	print('#'*100)
	print("You tried jumping the gate, impaling yourself on a spike and falling on the other side. You don't make it very far before you collapse and die.")
	player_obj.kill()

def sweptaway(player_obj):
	print('')
	art.display("sweptaway")
	print('#'*100)
	print("You've been swept away!")
	player_obj.kill()

def enter(player_obj, space_obj):
	art.display("bridge")
	if 'unlocked' in space_obj.options:
		print('#'*100)
		print('You are at the bridge you unlocked earlier.')
	else:
		print('#'*100)
		print("You find a bridge, the gate is locked. Maybe you have something that will open it?")

	while True:
		q = input('What would you like to do? ')
		if q.lower().split(' ')[0] == 'unlock' or 'key' in q.lower() or 'open' in q.lower():
			unlock(player_obj, space_obj)
		if q.lower().split(' ')[0] == 'jump' or 'climb' in q.lower():
			jump(player_obj)
			break
		else:
			err, rtext = query.parse_movement(q)
			if err == False:
				if rtext == 'forward' and 'unlocked' not in space_obj.options:
					print('You are unable to travel forward as the gate is locked.')
				elif rtext == 'right' or rtext == 'left':
					sweptaway(player_obj)
					break
				else:
					player_obj.move(rtext)
					break

def init():
	fieldspace = spatial.space()
	fieldspace.name = "bridge"
	fieldspace.enter = enter
	art.load("bridge", "content/bridge.ansi")
	art.load("blood", "content/blood.ansi")
	return fieldspace