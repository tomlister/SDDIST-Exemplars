import spatial
import art
import player
import query

def shoot(player_obj, space_obj):
	if 'beardead' not in space_obj.options:
		if 'shotgun' in player_obj.inventory:
			print("You shoot the bear, blowing a chunk of its head off. The bear lets off a final huff, slumps down and dies.")
			space_obj.options.append('beardead')
			player_obj.use('shotgun')
		else:
			print("You don't have anything to attack the bear with!")
	else:
		print('The bear is already dead.')

def bearattack(player_obj):
	print('The bear attacked you!')
	print('You slowly bled out...')
	player_obj.kill()

def enter(player_obj, space_obj):
	if 'beardead' not in space_obj.options:
		art.display("bear")
		print('#'*100)
		print('Oh no! A bear! It appears to be aggressive and will not let you pass.')
	else:
		art.display("field")
		print('#'*100)
		print("This is where you shot the bear. Its carcass is starting to decay.")

	while True:
		q = input('What would you like to do? ')
		if q.lower().split(' ')[0] == 'shoot' or q.lower().split(' ')[0] == 'kill':
			shoot(player_obj, space_obj)
		else:
			err, rtext = query.parse_movement(q)
			if err == False:
				if rtext == 'right' and 'beardead' not in space_obj.options:
					bearattack(player_obj)
					break
				else:
					player_obj.move(rtext)
					break

def init():
	fieldspace = spatial.space()
	fieldspace.name = "bear"
	fieldspace.enter = enter
	art.load("bear", "content/bear.ansi")
	return fieldspace