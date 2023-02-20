def search(arr, target=0):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1