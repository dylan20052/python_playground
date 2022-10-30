favorite_languages = {'jen': 'python', 
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python'}

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
	language.title() + ".")

# looping through all keys in a dictionary
for name in favorite_languages.keys():
	print(name.title())
	
	
friends = ['phil', 'sarah']
for name in favorite_languages:
	if name in friends:
		print("\nHi " + name.title() + ", I see your favorite language is " + 
		favorite_languages[name])
	else:
		print(name.title())
		
if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll!")

##################

favorite_languages = {
	'jen': ['python', 'ruby'], 
	'sarah': ['java', 'c'], 
	'edward': ['ruby'], 
	'phil': ['html', 'python']
	}
	
for n, l in favorite_languages.items():
	print(n.title() + "'s favorite languages are: ")
	for language in l:
		print("\t" + language.title())
