#In this question, you are given two strings, and you need to determine the minimum number of insertiom/deletion/swapping steps of the characters to convert string 1 to string 2.
#For example, str 1 = 'intention', str2 = 'execution' will require 5 swapping oprations on intertion to convert it into execution, swapping i to e, n to x, t to e, e to c and n to u.
#Recursion approach:- 
#If the first character is equal, then ignore and increment the pointer.
#If the first character is not equal, then 
#a. Either it has to be deleted :- 1 + Recursively solve after ignoring the first character of the string 1.
#b. Either it has to be swapped :- 1 + Recursively solve after ignoring the first character of each of the strings.
#c. Or a character inserted before :- 1 + Recursively solve after ignoring the first character of the string 2.
#Test Cases:-
#1) Equal length of the strings
#2) Unequal length of the strings
#3) One of the strings is empty
#4) Only deletion is required, only addition, or only swapping is required.
#5) A general case(listed above in the example)
#6) No change is required
#7) All the characters need to be changed.
def min_steps(str1, str2, i1, i2): #i1 and i2 are the pointers pointing to both the strings.
    print(str[i1:], str[i2:])
    if i1 == len(str1): #Edge or the trivial case, in which the str1 is empty, i.e., equal to 0.
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1) - i1
    elif str1[i1] == str2[i2]:
        return min_steps(str1, str2, i1+1, i2+1)
    else:
        return 1 + min(min_steps(str1, str2, i1+1, i2), min_steps(str1, str2, i1+1, i2+1), min_steps(str1, str2, i1, i2+1) #deleted, swapped, inserted.
        )
#Time Complexity, T(N) = O(3^(n1+n2)), n1 = len(str1), n2 = len(str2), since, three times recursive function is called.

#Optimised solution :-
#1) Using Memoization :-
def min_steps(str1, str2):
    memo = {}
    def recurse(i1, i2):
        key = i1, i2
        if key in memo:
            return memo[key]
        elif i1 == len(str1):
            memo[key] = len(str2) - i2
        elif i2 == len(str2):
            memo[key] = len(str1) - i1
        elif str[i1] == str[i2]:
            memo[key] = recurse(i1 + i2)
        else:
            memo[key] = 1 + min(recurse(i1 + 1, i2), recurse(i1 + 1, i2 + 1), recurse(i1, i2 + 1))
        return memo[key]
    return recurse(0, 0)
#Time Complexity, T(N) = O()