import spatial
import art
import player
import query

def enter(player_obj, space_obj):
	art.display("field")
	print('#'*100)
	print('You are in a field. Tall grass surrounds you.')
	while True:
		q = input('What would you like to do? ')
		err, rtext = query.parse_movement(q)
		if err == False:
			player_obj.move(rtext)
			break

def init():
	fieldspace = spatial.space()
	fieldspace.name = "field"
	fieldspace.enter = enter
	art.load("field", "content/field.ansi")
	return fieldspace