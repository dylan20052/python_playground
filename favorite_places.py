favorite_places = {'dylan': ['new jersey'], 'lauren': ['japan', 'new jersey', 'aruba'], 'nicole': ['plattsburgh', 'mississipi']}

for f, p in favorite_places.items():
	if len(p) == 1:
		print(f.title() + "'s favorite place is " + p[0].title())
	else:
		print(f.title() + "'s favorite places are")
		for place in p:
			print("\t" + place.title())
	
