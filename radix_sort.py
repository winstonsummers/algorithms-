arr = [2,5,1,6,8,4,2,1,5,7,9,0,9,5,33,11,167,8,2,4,336,56,21,5,6,7,8,26,123,44,-27,985,-3,45,292,-7,8,897,756,6,426,456,568,457,345,63,456,38,57,862,45,735,683,56,572,456,25,7,45,83,5672,454,1]

#flatten is a function soully to combine the nested lists into a single(flattened) list
def flatten(list_of_lists):
  #the list that will be returned after it is populated
  flattened = []
  #for each index in the main list
  for sublist in list_of_lists:
  	#for each index in a nested list
    for val in sublist:
    	#append the value to the flattened list to be returned
        flattened.append(val)
  #return the flattened list
  return flattened

#declare the sort function it takes a list and the length of the longest number(s)
def radix_sort(arr, max_digit):
	#declare the buckets a list of ten lists
	buckets = [[],[],[],[],[],[],[],[],[],[]]
	#declare the starting position of the sort(the one's place)
	digit_index = 0
	#for the number of times the list needs to be sorted (the 'k' in 'nk')
	for k in range(0, max_digit):
		print('outer, current digit: ', digit_index)
		#for the number of indexes in the list
		for i in range(0, len(arr)):
			#buckets at index which is equal to the list at index i divided by 
			#10 multiplied by the number of indexes all modulous 10
			#append arr at index i to that bucket
			buckets[((arr[i] // (10 ** digit_index)) % 10)].append(arr[i])
		#add one to the digit_index before the next iteration
		digit_index += 1
		print('buckets: ', buckets)
		# flatten and store the buckets
		arr = flatten(buckets)
		# reset the buckets
		buckets = [[], [], [], [], [], [], [], [], [], []]
	#return the stored buckets once they are finished sorting
	return arr

print('RESULTS: ',radix_sort(arr, 4))