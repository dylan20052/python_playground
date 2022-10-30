dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# looping through tuple values
for dimension in dimensions:
	print(dimension)
	
# writing over a tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
