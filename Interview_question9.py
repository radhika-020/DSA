#Given an array, and a value of k, we need to find the kth largest element from the array. For example, arr= [1, 2, 3, 4, 5, 6, 7], and k =3, then in this case, 1st largest element is 7, second largest element is 6 and the third largest element is 5. Therefore, we need to return 5.

def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

#In this question, we used an approach as we need to fi d the kth largest element in the list, therefore, at first, using loop, we are removing the k-1 largest elements from the array. Then, at the end of the loop, we are left with the array which has the kth largest element. Therefore, in that case, return the max element of the array.