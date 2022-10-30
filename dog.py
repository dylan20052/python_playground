class Dog():
	"""A simple attempt to model a dog."""
	
	def __init__(self, name, age):
		"""Init name and age"""
		self.name = name
		self.age = age
		
	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")

my_dog = Dog('piper', 5)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
