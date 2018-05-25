def the_merge(arr1, arr2):
	results = []
	while len(arr1) > 0 and len(arr2) > 0:
		if arr1[0] > arr2[0]:
			results.append(arr2.pop(0))
		else:
			results.append(arr1.pop(0))
	print('the merge',results + arr1 + arr2)
	return results + arr1 + arr2

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	else:
		middle_index = len(arr) // 2
		left = arr[:middle_index]
		right = arr[middle_index:]
		left_sorted = merge_sort(left)
		right_sorted = merge_sort(right)
		return the_merge(left_sorted, right_sorted)

my_list = [2,5,1,6,8,4,2,1,5,7,9,0,9,5,33,11,167,8,2,4,336,56,21,5,6,7,8,26,123,44,-27,985,-3,45,292,-7,8,897,756,6,426,456,568,457,345,63,456,38,57,862,45,735,683,56,572,456,25,7,45,83,5672,454,1]

print(merge_sort(my_list))