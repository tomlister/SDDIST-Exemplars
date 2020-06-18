import spatial
import art
import player
import query
import random
import time

def monster(player_obj, space_obj):
	playerhealth = 100
	monsterhealth = 100
	print('A monster from the depths of the forest has attacked you!')
	print('You can (fight) or try your luck at running (run).')
	while True:
		print('Your health: '+str(playerhealth))
		print("Monsters health: "+str(monsterhealth))
		q = input('What would you like to do? ')
		if q.lower() == 'fight':
			if random.random() < 0.35:
				print("You hit the monster.")
				monsterhealth -= 10
			elif random.random() < 0.50:
				print("The monster hit you.")
				playerhealth -= 10
			else:
				print("Nothing happened.")
		elif q.lower() == 'run':
			if random.random() < 0.25:
				print("Your attempt to flee was unsuccessful.")
				playerhealth = 0
				player_obj.kill()
				break
			else:
				print("Your attempt to flee was successful.")
				break
		if playerhealth <= 0:
			break
	if playerhealth <= 0:
		print('You died.')
		return True


def enter(player_obj, space_obj):
	art.display("forest")
	print('#'*100)
	print("You are in a forest. Tall trees tower over you. You feel goosebumps on your skin, something doesn't feel right.")
	time.sleep(3)
	if random.random() < 0.45:
		if monster(player_obj, space_obj) == False:
			while True:
				q = input('What would you like to do? ')
				err, rtext = query.parse_movement(q)
				if err == False:
					player_obj.move(rtext)
					break
	else:	
		while True:
			q = input('What would you like to do? ')
			err, rtext = query.parse_movement(q)
			if err == False:
				player_obj.move(rtext)
				break

def init():
	fieldspace = spatial.space()
	fieldspace.name = "forest"
	fieldspace.enter = enter
	art.load("forest", "content/forest.ansi")
	return fieldspace