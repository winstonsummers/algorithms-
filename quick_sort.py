#define the quick sort function
def quick_sort(list):
	#declare the case statement
	#if the list being passed in is longer than 1
	if len(list) <= 1:
		#then it is sorted return that list
		return list
	#other wise it is longer than 1 and needs to be broken down farther
	else:
		#the pivot is the value at index zero removed
		pivot = list.pop(0)
		#left is everything of lesser value in the current list
		left = [x for x in list if x < pivot]
		#right is everything of greater value in the current list
		right = [x for x in list if x >= pivot]
		#print is the check my work
		print('left', left, 'pivot', pivot, 'right', right)
		#the end is a recursive statement that will return the original list sorted
		return quick_sort(left) + [pivot] + quick_sort(right)

my_list = [2,5,1,6,8,4,2,1,5,7,9,0,9,5,33,11,167,8,2,4,336,56,21,5,6,7,8,26,123,44,-27,985,-3,45,292,-7,8,897,756,6,426,456,568,457,345,63,456,38,57,862,45,735,683,56,572,456,25,7,45,83,5672,454,1]

print(quick_sort(my_list))