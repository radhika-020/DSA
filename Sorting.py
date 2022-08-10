#In sorting, we need to check the following set of cases while sorting a list of numbers.
#1) Some lists of nubers in random order.
#2) A list that's already sorted.license
#3) A list that's sorted in descending order.
#4) A list containing repeating elements.
#5) An empty list.
#6) A list containing just one element.
#7) A list containing one element repeated many times.
#8) A really long list. 

#Bubble Sort
from heapq import merge


def bubble_sort(nums):
    nums = list(nums) #converting the input to the list.
    for _ in range(len(nums)-1):
        for i in range(len(nums)-1): #Iteration will be till n-1 elements, because at the very first iteration, the largest number will get into its oiginal place, i.e., at the end.
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i] #swapping the two elements, if the index i + 1 is less than the index i.
    return nums #returns the sorted list
#Time Complexity = (n-1)*(n-1) = n^2 -2n +1
#Therefore, T(N) = O(N^2)
#Space Complexity = O(1), because, the range function only takes 1 element at a time.
#Roughly, S(N) of bubble sort is O(N).

#Insertion Sort
def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        current = nums.pop(i)#one value is popped(deleted) from the nums, and stored in the current, can also be written as current = nums[i].
        j = i-1
        while j>=0 and nums[j]>current: #value in current is compared with the value at nums[j]
            j = j-1
        nums.insert(j+1, current)
    return nums

#Merge Sort
def merge_sort(nums):
    if len(nums)<=1: #len(nums)<2
        return nums
    mid = len(nums)//2
    left = [:mid] #slicing, from 0 index position to mid - 1.
    right = [mid:]
    left_sorted, right_soted = merge_sort(left), merge_sort(right)
    #Combining the left and right sorted lists
    sorted_nums = merge(left_sorted, right_soted)
    return sorted_nums

#Merge function to merge the two sorted lists.
def merge(nums1, nums2):
    merged = []#An empty list is created to store the result of the sorted two arrays, nums1 and nums2.
    i, j = 0, 0 #For iterating in both the lists, their initial pointers are kept at the indices 0.
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <  nums2[j]:
            merged.append(nums1[i]) #if the value in nums1 list, at ith index is smaller than the value at the jth index in nums2, then append in the empty list and then increment the i by 1 each time or else vice versa.
            i = i+1
        else:
            merged.append(nums2[j])
            j = j+1
            #While loop will end at the condition where one of the condition gets False, i.e., one of the lists gets finished.
            #get the remaining parts of the lists by:-
        nums1_tail = nums1[i:] #if nums2 exceeded out of limit, then getting the list nums1 from ith index to the last and adding it in the final merged list or vice versa.
        nums2_tail = nums2[j:]
        return merged + nums1_tail + nums2_tail 
#Time Complexity, T(N) = O(NlogN)
#Space Complexity = O(N)

#Quick Sort, this is far more better than all the other sorting techniques mentioned above.
def quick_sort(nums, start = 0, end = None):
    if end is None:
        nums = list(nums) #making a copy of the input list here, at the beginning only.
        end = len(nums)-1
    if start < end: #which menas the list has more than one element, in the case, when start = end, means that there is only one element present in the list.
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)
    return nums

#Partition function
def partition(nums, start = 0, end = None): #This function returns the position of the pivot.
    if end is None:
        end = len(nums) - 1
#We are taking the end element as a pivot, so initialising a left pointer which will point to the first element of the list, and a right pointer which will point to the end - 1, i.e., the element right before the pivot element of the list, and then comparing the first and end-1 element.
    left, right = start, end-1
    while right > left:
        if nums[left] <= nums[end]: #Increment left pointer if the start element is less or equal to the pivot.
            left = left + 1
        elif nums[right] > nums[end]: #Decrement right pointer if number is greater than the pivot.
            r = r -1
            #Otherwise, the two  of them, i.e., the left and right pointers are out of place, therefore they can be swapped.
        else:
            nums[left], nums[right] = nums[right], nums[left]
    if nums[left]>nums[right]: #Place the pivot element between the two parts.
        nums[left], nums[end] = nums[end], nums[left]
        return left
    else:
        return end
#Time Complexity = O(NlogN), average case complexity.
#T(N) = O(N^2), worst case complexity
#T(N) depends upon choosing the pivot element, if we choose the smallest element as pivot, this will lead to the worst case complexity.