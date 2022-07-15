#0-1 Knapsack Problem, is a problem in which weights are given with their respective properties, and we have to select items such that the weights of the item are less than or equal to the capacity and should give the maximum profit, in 0-1 Knapsack, the item can either be chosen or dropped, but cannot be chosen in fraction unlike fractional Knapsack.
#Test cases:-
#1) Some generic test cases
#2) All the elements caan be included.
#3) None of the elements can be included.
#4) Only one of the elements can be included.
#5) You do not use the complete capacity.
#Recursive solution:
def max_profit_recursive(weights, capacity, profits, index = 0):
    if index == len(weights): #base condition, i.e., if index = 0 is equal to the length of the weights, i.e., 0, then we can return 0.
        return 0
    elif weights[index] > capacity: #if the element at index have weight greater than the capacity, then it cannot be included in the Knapsack, therefore calleed recursive function on index+1 with same capacity.
        return max_profit_recursive(weights, capacity, profits, index+1)
    else:
        option1 = max_profit_recursive(weights, capacity, profits, index+1) #one option is that the element can be fitted inside the knapsack, i.e., its weight <= capacity, but it cannot be included because it is not giving the maximum profit, therefore again calling the recursive function with index+1 and same capacity left.
        option2 = profits[index] + max_profit_recursive(weights, capacity - weights[index], profits, index+1) #another option is that the element at that specific index is selected, therefore the profit of that index will also be added and the recursive function will be called on index+1 with capacity - weights[index].
        return(option1, option2)
#%%time is used to determine the time of the computation.
#Time Complexity, T(N) = O(2^N), exponential complexity because we are computing things repeatedly.
#Apply memoization, note that capacity and index are changing, therefore, they can be stored in the memo dictionary.
#Dynamic Programming solution:-
def max_profit_dp(weights, profits, capacity):
    n = len(weights) #n is initialised as len(weights) because of creating a table.
    table = [[0 for _ in range(capacity+1) for _ in range(n+1)]] #this will create a table of n+1 rows and capacity+1 rows with initial values as 0, and n+1 and capacity+1 is taken due to an extra row or column which will remain 0 throughout the program.
    for i in range(n):
        for c in range(1, capacity): #capacity starts with 1 because we do not to alter the first initialised column of capacity as 0.
            if weights[i] > c:
                table[i+1][c] = table[i][c] #if weights at i is grreater than the in place capacity of that specific column, then the value from the upper row and same column is copied at the same index of table[i+1][c].
            else:
                table[i+1][c] = max(table[i][c], profits[i] + table[i][c - weights[i]]) #first option is that we do not select the element because it does not gives the optimal solution, and the second option is we select the element, by adding the profits and decreasing the remaining capacity by weights[i].
    return table[-1][-1] #returns the last element of the table.
#Time Complexity, T(N) = O(N*W)   