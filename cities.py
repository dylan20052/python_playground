cities = {
	'delray beach': {'state': 'florida', 'population': 50000, 'fact': 'most beautiful city in us'}, 
	'princeton': {'state': 'new jersey', 'population': 30000, 'fact': 'highest indian population in us'}, 
	'los angeles': {'state': 'california', 'population': 100000, 'fact': 'most famous people in us'}
	}

for city, city_info in cities.items():
	print("\n" + city.title())
	for info, stat in city_info.items():
		print("\t" + info + ": " + str(stat))
		
