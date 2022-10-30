everything = ['english', 'spanish', 'french', 'mount vesuvius', 'mount kilaminjaro', 'new york city', 'delray beach', 'africa', 'america']

print(len(everything))

print(everything)
print(sorted(everything))

print(everything)
print(sorted(everything, reverse=True))

print(everything)
everything.reverse()
print(everything)
everything.reverse()
print(everything)

everything.sort()
print(everything)
everything.sort(reverse=True)
print(everything)

# Adding to an array
everything.append('china')
print('\n' + str(everything))

everything.insert(3, 'volcano')
print(str(everything))

# Removing from an array
popped_everything = everything.pop(5)
print('\n' + popped_everything)
print(everything)

del everything[2]
print('\n' + str(everything)) 
