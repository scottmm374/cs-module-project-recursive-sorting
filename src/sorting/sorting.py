# TO-DO: complete the helper function below to merge 2 sorted arrays
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        copy_left = []
        copy_right = []

        merge_sort(left)
        if len(left) == 1:
            print("only one on left")
            copy_left.append(left[0])

        merge_sort(right)
        if len(right) == 1:
            print("only one on right")
            copy_right.append(right[0])


merge_sort(arr1)
# ! STRETCH: implement the recursive logic for merge sort in a way that doesn't
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists
# # or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
