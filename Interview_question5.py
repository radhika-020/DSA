#https://www.interviewbit.com/problems/disjoint-intervals/

class solution:
    def solve(self, A):
        A.sort(key=lambda x: x[1]) #We are sorting the array with its last index, for example, array = [[1, 2], [2, 10], [4, 6]], we are sorting this as [[1, 2], [4, 6], [2, 10]], i.e., by the last index, the x[0][1].
        prev_s, prev_e = A[0] #Storing the previous starting and ending values and always including it in the start.
        count = 1 #Count is always 1 because the first element is always included.

        for s, e in A: #Iterating over starting and ending values of all the elements.
            if s<=prev_e: #We are checking here that the current element we are looking at has a value smaller or equal than the previous ending element, then it will overlap if we include this element, therefore, this will not be in the disjoint intervals. Therefore, neglecting this condition simply by writing pass.
                pass
            else:
                prev_s, prev_e = s, e #Or else, we are including the current element, and now making it the previous element by assigning it to previous starting and previous ending, and incrementing the count by 1 in that case.
                count += 1
        return count