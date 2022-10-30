# A simple dictionary

alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])

# accessing values in dictionary
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!") 

# adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


# modifying values in a dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


# tracking position of alien
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))

	# moves alien to right
	# determine how far to move the alien based on its current speed
	
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


# removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print("\n" + str(alien_0))

del alien_0['points']
print(alien_0)

# nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

	# more realistic version of nesting
	
aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")

print("The total number of aliens: " + str(len(aliens)))
