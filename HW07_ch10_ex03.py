# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(list_of_nos):
	cum_sum = 0
	for idx in range(0,len(list_of_nos)):
		cum_sum += list_of_nos[idx]
		list_of_nos[idx] = cum_sum

def main():
	list_of_nos = [1, 2, 3, 6]
	cumulative_sum(list_of_nos)
	print(list_of_nos)

if __name__ == "__main__":
	main()