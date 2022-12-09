# Python3 Program for recursive binary search.

# Returns index of x in array_to_search if present, else -1


def binary_search(array_to_search, start_index, last_index, x):

	# Check base case
	if last_index >= start_index:

		mid = (start_index + last_index) // 2
		print("mid =",  mid)
		# If element is present at the middle itself
		if array_to_search[mid] == x:
			return mid

		# If element is smaller than mid, then it
		# can only be present in left subarray
		elif array_to_search[mid] > x:
			print("Start index:%s Last Index:%s" % start_index, mid-1)
			return binary_search(array_to_search, start_index, mid - 1, x)

		# Else the element can only be present
		# in right subarray
		else:
			print("Start index:%s Last Index:%s" % (mid + 1,last_index))
			return binary_search(array_to_search, mid + 1, last_index, x)

	else:
		# Element is not present in the array
		return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index % d" % result)
else:
	print("Element is not present in array")
