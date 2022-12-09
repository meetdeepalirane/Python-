def reverse(arr):
    if not arr:
        return []
    return [arr[-1]]+reverse(arr[:-1])

li=[1,2,3,4,5,6]
print(reverse(li))