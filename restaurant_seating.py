prompt = "How many people are in your dinner group? "
number_of_people = int(input(prompt))

if number_of_people > 8:
	print("\nYou'll have to wait for a table.")
else:
	print("\nYour table is ready.")
