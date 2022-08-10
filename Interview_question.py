#You are given an array, and a target sum, you need to fund a contiguous array indices, which results to the given sum. This is s greedy approach solution.
#For example, arr = [1, 2, 3, 4, 5, 6, 7], target sum = 9, therefore, the contiguous array resulting in sum 9 will be [2, 3, 4] from indices 1 to 4(4 not included), therefore, the output should be 1, 4.
#Test Cases to be kept in mind:-
#1) Generic array, subarray occurring somewhere in the between.
#2) Subarray could be at the starting of the given array.
#3) Subarray could be at the end of the given array.
#4) There is no subarray resulting in the target sum.
#5) You have a few zeros in the array/list.
#6) There are multiple subarrays resulting in the same target sum.
#7) The array is empty.
#8) The subarray is a single element.
#A bruteforce solution.
def subarray_sum(arr, sum):
    n = len(arr)
    #i goes from 0 to n-1, iterating over the full array.
    for i in range(0, n):
        #J goes from i to N+1, because, in the j index, we also need to return the position of the element which is not included, like as in the rage function, the last index is not included.
        for j in range(i, n+1):
            if sum(arr[i:j]) == sum:
                return i, j
    return None, None
#Time Complexity, T(N) = O(n^3)

#Optimised solutions:-
#1) Maintain a running sum for the inner loop
#2) When sum exceeds the target sum , break the inner loop.

#1) This solution keeps a track of sum, nand the place where initialised sum becomes equal to the target sum, we simply return the sum.
def subarray_sum1(arr, sum):
    n = len(arr)
    for i in range(0, n):
        s = 0 #running sum
        for j in range(i, n+1):
            if s == sum:
                return i, j
            elif s > sum: 
                break
            if j < n: #This is done beacuse the j loop is taking the n element as well.
                s = s + arr[j] #which means the sum is still less than the target sum.
    return None, None
#Time Complexity, T(N) = O(n^2)

#2)
def subarray_sum(arr, sum):
    n = len(arr)
    i, j, s = 0, 0, 0
    while i < n and i < n+1:
        if s == sum:
            return i, j
        elif s < sum:
            s = s + arr[j] #keep incrementing j while keeping i the same.
            j = j+1    
        elif s > sum:
            s = s - arr[i] #The moment where the sum becomes greater then the target sum, then decrease the value of i from the sum, and increment i.
            i = i+1
    return None, None
#Time Complexity, T(N) = O(N)