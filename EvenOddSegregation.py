def segregateEvenOdd(arr):
    # Initialize left and right indexes
    left, right = 0, len(arr) - 1

    while left < right:

        # Increment left index while we see 0 at left
        while (arr[left] % 2 == 0 and left < right):
            left += 1

        # Decrement right index while we see 1 at right
        while (arr[right] % 2 == 1 and left < right):
            right -= 1

        # while(arr[left] % 2 != 1 and left<right):
        #     left=left+1

        if left < right:
            # Swap nb arr[left] and arr[right]*/
            arr[left], arr[right] = arr[right], arr[left]
            right = right - 1
            left += 1

# Driver function to test above function
arr = [12, 34, 45, 9, 8, 90, 3]
print (arr)
segregateEvenOdd(arr)
print(" Array after segregation ", arr)
