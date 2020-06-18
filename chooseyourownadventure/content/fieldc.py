import spatial
import art
import player
import query

def dig(player_obj, space_obj):
	if 'found_key' not in space_obj.options:
		print('You dig... and find a \033[91;40;1mkey.\033[0m')
		player_obj.give('key')
		space_obj.options.append('found_key')
	else:
		print("You've already dug here.")
def enter(player_obj, space_obj):
	art.display("field")
	print('#'*100)
	print('You are in a field. Tall grass surrounds you. The ground seems to be recently disturbed.')
	while True:
		q = input('What would you like to do? ')
		if q.lower() == 'dig':
			dig(player_obj, space_obj)
		else:
			err, rtext = query.parse_movement(q)
			if err == False:
				player_obj.move(rtext)
				break

def init():
	fieldspace = spatial.space()
	fieldspace.name = "fieldc"
	fieldspace.enter = enter
	art.load("field", "content/field.ansi")
	return fieldspace