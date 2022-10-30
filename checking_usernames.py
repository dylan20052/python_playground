current_users = ['admin', 'Dylan', 'name', 'myusername', 'Marie0820']

new_users = ['dylan', 'jerry', 'Gerald', 'myUSERname', 'berries']

for current_user in range(len(current_users) - 1):
	current_users[current_user] = current_users[current_user].lower()
	
for new_user in new_users:
	if new_user.lower() in current_users:
		print(new_user + " has been taken.")
	else:
		print(new_user + " is available")
