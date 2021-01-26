# TO-DO: complete the helper function below to merge 2 sorted arrays
arr1 = [1, 5, 8, 4, 2, 9, 6, 0]
# copy_left = []
# copy_right = []


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # variables to keep track of index
    left = 0
    right = 0
    i = 0

#  for each item in sub arrays, while index in each are less then length of each array.
    while left < len(arrA) and right < len(arrB):
        # comparing indicies in each sub array
        if arrA[left] <= arrB[right]:
            # replacing merged[i] with arrB value at index
            merged_arr[i] = arrA[left]
            left += 1
            # replacing merged[i] with arrA value at index
        else:
            merged_arr[i] = arrB[right]
            right += 1

        i += 1

    while left < len(arrA):
        merged_arr[i] = arrA[left]
        left += 1
        i += 1

    while right < len(arrB):
        merged_arr[i] = arrB[right]
        right += 1
        i += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Base: array with only 1 element
    if len(arr) <= 1:
        return arr

    # Find mid point and break up arrays into two halves.
    middle = len(arr) // 2
    arrA = arr[:middle]
    arrB = arr[middle:]

    # call merge recursivly on each half, and continue until they are one value each
    return merge(merge_sort(arrA), merge_sort(arrB))


x = merge_sort(arr1)
print(x)


# ! STRETCH: implement the recursive logic for merge sort in a way that doesn't
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists
# # or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
