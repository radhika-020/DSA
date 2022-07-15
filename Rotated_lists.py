#In the above question of rotated lists, we are given a list which is sorted ad rotated an unknown number of times, we need to find the minimum number of times that rotated list need to be rotated more so that the original list is obtained.
# For eg, given a list nums = [1, 2, 3, 4, 5, 6] is rotated 3 times, then the rotated list will be [4, 5, 6, 1, 2, 3].
#A rotated list is alist in which the last element of the list comes at the starting position, say for instance, nums = [1, 2, 3, 4] is rotated 1 time, then the rotated list will be, [4, 1, 2, 3].
#Another point to be noted in the rotating list is that if we want to find the number of times it was rotated, then simply return the position of the smallest number in the rotated list. Say, for in the first examplem 1 is the smallest number and is at the position 3 from the beginning, therefore, we can determine that the list was rotated 3 times. In the full list, it will be the only number, which is smaller than its predecessor or the number coming before it.

#This solution is done in the linear search approach.
def rotation(nums):
    #nums is the rotated sorted list which is provided as input.
    position = 0
    while nums<len(nums):
        if position> 0 and nums[position]<nums[position-1]:
            return position
        else:
            position = position+1
    return 0 # if the above condition does not satisfies, that means the list is rotated 0 times, or if the position passed the length of the input list, therefore, returning 0.


#This solution is done in the binary search approach. In binary search, the middle element is determined, if the middle element is the smallest element in the list, and is the only number thta is smaller than the number before it, then return the position, i.e., mid. Or if the middle element is not the one, then check for the condition that the position of the smallest number lies at the right or left of the list. If the middle elemnt is smaller then the element at the last index, then return 'left' else return 'right'
def roration(nums):
    low=0
    high = len(nums)-1
    while low<=high:
        mid = (low+high)//2

        if mid>0 and nums[mid]<nums[mid-1]:
            return mid
        elif nums[mid]<nums[high]:#nums[high] is the last index of the list.s
            high = mid-1 #return 'left'
        else:
            low = mid+1 #return 'right'
    return 0
