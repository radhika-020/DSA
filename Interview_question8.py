#Given a sorted array, we need to find the first and last position of the target given. For example, arr = [2, 4, 5, 5, 5, 5, 5, 6, 7, 8], target = 5, therefore, the value 5 started at index 2 and ended at index 6, therefore we need to return [2, 6].
#Using Linear Search approach.

def index_positions(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
    return [-1, -1] #In cas, we do not find the start and end indices. Time complexity = O(N)


#OR using binary search approach.

def find_start(arr, target):
    if arr[0] == target:
        return target
    left, right = 0, len(arr) - 1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] <= target:
            left = mid+1
        else:
            right = mid-1
    return -1

def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1
    while left<=right:
        mid = (left+mid)//2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

def find_and_start(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end] #Time Complexity = O(NlogN)