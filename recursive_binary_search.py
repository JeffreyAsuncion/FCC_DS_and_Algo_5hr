def recursive_binary_search(list, target):
    if len(list) == 0:
        return -1

    mid = (len(list))//2

    if list[mid] == target:
        return mid
    elif list[mid] > target:
        recursive_binary_search(list[:mid], target)
    else:
        recursive_binary_search(list[mid+1:], target)

    return -2



def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers = [1,2,3,4,5,6,7,8,9,10]
target = 5

result = recursive_search(numbers,12)
verify(result)

result = recursive_search(numbers,6)
verify(result)