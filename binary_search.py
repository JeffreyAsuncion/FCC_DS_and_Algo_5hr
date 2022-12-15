def binary_search(list, target):

    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left+right)//2

        if list[mid] == target:
            return mid
        elif list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1 

    return -1



def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers = [1,2,3,4,5,6,7,8,9,10]
target = 5

result = binary_search(numbers,12)
verify(result)

result = binary_search(numbers,6)
verify(result)