# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(list_of_elements):
	if len(list_of_elements) < 2:
		return True
	for idx in range(0, len(list_of_elements) - 1):
		if list_of_elements[idx] > list_of_elements[idx + 1]:
			return False
	return True

def main():
	list_of_nos = [1, 2, 3, 6]
	list_of_chars = ['a', 'c' , 'b']
	print(is_sorted(list_of_nos))
	print(is_sorted(list_of_chars))

if __name__ == "__main__":
	main()