def shoot(player_obj, space_obj):
	if 'shotgun' in player_obj.inventory:
		print("You fire a shot using the last cartridge.")
		player_obj.use('shotgun')
	else:
		print("You don't have anything to shoot with.")