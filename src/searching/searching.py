# TO-DO: Implement a recursive implementation of binary search
arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]


start_index = 0
end_index = len(arr1) - 1


def binary_search(arr, target, start, end):

    if len(arr) == 0:
        return -1

    mid_index = (start + end) // 2
    mid_val = arr[mid_index]

    if target == mid_val:
        return mid_index

    if target != mid_val:

        if target > mid_val:
            if start == mid_index:
                return -1
            else:
                start = mid_index
                return binary_search(arr, target, start, end)

        if target < mid_val:
            if end == mid_index:
                return -1
            else:
                end = mid_index
                return binary_search(arr, target, start, end)


x = binary_search(arr1, -10, start_index, end_index)
print(x)


# !STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively

# def agnostic_binary_search(arr, target):
#     # Your code here
