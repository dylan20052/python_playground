def describe_pet(pet_name, animal_type='dog'):
	"""Display pet info."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

# bypassing default parameter
describe_pet(pet_name='gerald', animal_type='hamster')
