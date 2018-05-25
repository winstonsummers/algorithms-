def radix_sort(arr, max_digit):
	buckets = make_buckets()
	current_digit = 1
	for i in range(0, max_digit):
		for j in range(0, len(arr)):
			sig_digit = arr[j] // current_digit 
			buckets[sig_digit % 10].append(arr[j])
		arr = flatten(buckets)
		buckets = make_buckets()
		current_digit *= 10
	return arr

def flatten(list_of_lists):
	flattened = []
	for sublist in list_of_lists:
		flattened.extend(sublist)
	return flattened

def make_buckets():
	buckets = []
	for i in range(0, 10):
		buckets.append([])
	return buckets

my_list = [2,5,1,6,8,4,2,1,5,7,9,0,9,5,33,11,167,8,2,4,336,56,21,5,6,7,8,26,123,44,-27,985,-3,45,292,-7,8,897,756,6,426,456,568,457,345,63,456,38,57,862,45,735,683,56,572,456,25,7,45,83,5672,454,1]

print(radix_sort(my_list, 4))