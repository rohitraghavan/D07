# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(list_of_animals):
	for index in range(0, len(list_of_animals)):
		if type(list_of_animals[index]) is list:
			list_of_animals[index] = capitalize_nested(list_of_animals[index])
		elif type(list_of_animals[index]) is str:
			list_of_animals[index] = list_of_animals[index].capitalize()
	return list_of_animals

def main():
	list_of_animals = ['apple', ['bear', ['fish', 'chicken']], 'cat']
	capitalize_nested(list_of_animals)
	print(list_of_animals)

if __name__ == "__main__":
	main()
