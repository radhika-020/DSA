#https://www.interviewbit.com/problems/highest-product/

class Solution:

    def highest_product(self, A):
        A = sorted(A)

        highest3 = A[-1] * A[-2] * A[-3]
        two_low_one_high = A[0] * A[1] * A[-1]

        return max(highest3, two_low_one_high)

#This problem is about having an array and returning the highest product that can be obtained by multiplying three numbers of the array. In the first case, when the array is sorted, and have the positive values, in that case, the last three elements will be the highest, therefore, multiplied last three in the frst variable.
#In the second case, for say we are given a sorted array as [-5, -2, -1, 0, 1, 1, 5], here, if we take the last three highest elements, we will get a product of 5, which is not the highest. The highest product here should be, -5*-2*5, therefore, the second variable deals with the same comdition.
#And at the end, we are returing the max or the highest value from both the variables.