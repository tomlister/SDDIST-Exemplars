import spatial
import art
import player
import query

def sweptaway(player_obj):
	print('')
	art.display("sweptaway")
	print('#'*100)
	print("You've been swept away!")
	player_obj.kill()

def enter(player_obj, space_obj):
	art.display("river")
	print('#'*100)
	print('You are on the edge of a river, it is unsafe to cross.')
	while True:
		q = input('What would you like to do? ')
		err, rtext = query.parse_movement(q)
		if err == False:
			if rtext == 'forward' or rtext == 'right' or rtext == 'left':
				sweptaway(player_obj)
				break
			else:
				player_obj.move(rtext)
				break

def init():
	riverspace = spatial.space()
	riverspace.name = "river"
	riverspace.enter = enter
	art.load("river", "content/river.ansi")
	art.load("sweptaway", "content/sweptaway.ansi")
	return riverspace