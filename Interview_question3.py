#https://www.interviewbit.com/problems/interview-questions/
#Time Complexity : O(N), N is the number of bulbs.
#Space Complexity : O(1) for the cost variable.

class Solution:
    def bulbs(self, A):
        cost = 0

        for b in A: #For every bit in the array A
            if cost%2 == 0:
                b = b
            else: 
                b = not b

            if b%2 == 1:
                continue
            else:
                cost += 1
        return cost

#This pproblem states that whenever we encounter a 0 bit in the array, we need to flip all the right hand side bits including that bit. Therefore, the logic used here is, when the cost will be 2, then again flipping the bits will ultimately get us te original array. Therefore, we need not to flip the bits in that case and b is assigned to b then. And, when the bit 1 is encountered, then in that case, the loop continues, and if bit 0 is encountered then along with the flipping operation, cost is also increased by 1.