#LCS or Longest Common Subsequence is a problem in which two or more strings or lists are given, and we have to find the length of the longest common subsequence that can occur in between them.
#For example, given two strings named as
#seq1 = dense, seq2 = condensed
#In the above sequences, dense is the most common and the largest sequence that is occurring in both the sequences, and is occurring linearly, i.e., in sequence from starting to end.
#We are to write a code to determine the longest common subsequence that might occur between two sequences, and note that there may occur chances that no common susequence may occur, or one of the two sequences is empty, or both are empty, in that case, we have to return 0.


def lcs_recursive(seq1, seq2, index1 = 0, index2 = 0): #In both the sequences, a pointer is set at the starting index of both the sequences, therefore initialised to 0.
    if len(seq1) == index1 or len(seq2) == index2: #whih means if the first index is the length of both the sequences or any of the two sequences is empty, then return 0, therefore used or opeartion here.
        return 0
    elif seq1[index1] == seq2[index2]:
        return 1 + lcs_recursive(seq1, seq2, index1+1, index2+1) #incremented both the indices because we found a common character and nw we need to check for the index+1.
    else:
        option1 = lcs_recursive(seq1, seq2, index1+1, index2) #incremented index1 by keeping index2 at 0 only because there might be chances that the character at index1 is not in the lcs and vice versa done for index2(option2).
        option2 = lcs_recursive(seq1, seq2, index1, index2+1)
        return max(option1, option2)
#Time Complexity, T(N) = O(2^m+n) 

#but this functon is quite inefficient, therefore, getting it more eficient,
#It is inefficient, because there are trees which are repeating more than once causing inefficiency,
#now using the approach Memoization in which a dictionary is created(to store the intermediate results), and a key is created with both the indices, at the first, the key with both the indices is checked if it is present in they memo[key], then the memo[key] is returned or else the three above steps are performed of lcs_recursive function but using memo[key].
def lcs_memo(seq1, seq2):
    memo = {} #an empty dictionary to store the key values.
    def recurse(index1 = 0, index2 = 0):
        key = (index1, index2)
        if key in memo:
            return memo[key]
        elif len(seq1) == index1 or len(seq2) == index2:
            memo[key] = 0
        elif seq1[index1] == seq2[index2]:
            memo[key] = 1 + recurse(index1 + 1, index2 + 2)
        else:
            memo[key] = max(recurse(index1 + 1, index2), recurse(index1, index2 + 1))
        return memo[key]
    return recurse(0, 0)
#Time Complexity, T(N) = O(mn)

#More Optimised Solution is Dynamic Programming(DP) in wwhich rather a dictionary, a matrix or table is created of size n2+1 and n2+1 where n1 and n2 are length of seuences 1 and 2 respectively, and table[i][j] represents the LCS f seq1[:i] and seq[:j].
#The table that we want to create initially shoyld contain all the 0s and this can be made using,
#[[0 for x in range(n2)] for x in range(n1)], lets just say that n1 = 5, n2 = 7, therefore, the table will contain 5 rows as for n1 and 7 columns as for n2 all containing 0 initially.
def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for x in range(n2+1)] for x in range(n1+1)] #created for n1+1 and n2+1 because we ned an extra row and column for storing the 0 values which will remain 0 throughout our program.
    for i in range (n1): #For iterating over the rows
        for j in range(n2): #For iterating over the columns
            if seq1[i] == seq2[j]:
                table[i+1][j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i+1][j], table[i][j+1])
    return table[-1][-1] #This returns the last element of the table.
#Time Complexity, T(N) = O(n1n2)
#Since, it does not call any other function inside it, therefore, it also takes lesser memory then memoization and recursion approach.