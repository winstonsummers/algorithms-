def binary_search(sorted_arr, target_value):
	# Set min/max indexes. start with all indexes in play
	min = 0
	max = len(sorted_arr) - 1

	# Keep narrowing down search untill found target_value or no where left to look
	while(min <= max):
		# Set up guess
		guess = (min + max) // 2

		# Check arr at guessed index for target. if not adjust range
		if sorted_arr[guess] == target_value:
			return guess # Found value
		elif sorted_arr[guess] < target_value:
			min = guess + 1 # Move up the min
		else:
			max = guess - 1 # Move down the max

	# Outside the loop- watch out for indetation!
	# If we ever get this far it's because we didn't fine the target
	return -1


# Hello from the Outside of the function
# Let's make some test data
tester = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]

testy = 20

# See what do!
print(binary_search(tester, testy))