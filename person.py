person = {'first_name': 'dylan', 'last_name': 'mcclish', 'age': 13, 'city': 'delray beach'}
person_1 = {'first_name': 'lauren', 'last_name': 'howarth', 'age': 24, 'city': 'nagasaki'}
person_2 = {'first_name': 'nicole', 'last_name': 'foss', 'age': 24, 'city': 'plattsburg'}
people = [person, person_1, person_2]

for p in people:
	print("\nFull Name: " + p['first_name'].title() + " " + p['last_name'].title())
	print("Age: " + str(p['age']))
	print("City: " + p['city'])
