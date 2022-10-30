players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# looping through a slice

print("\nHere are the first three players:")
for player in players[:3]:
	print(player.title())
