#cards = list of numbers in descending order, for instance, [12, 11, 10, 9, 8, 7] etcetera.
#query = a number, whose position is to be determined, for instance, 10.
#position = the position of the queried number, for instance, 2 for number 10.

#def locate_card(cards, query):
    #pass

#Dictionaries can also be used in this.
#test = { 'input' : {'cards': [12, 11, 10, 9, 8, 7], 'query': 10}, 'output': 2}
#locate_card(**test['input']) == test['output']
#In case of dictinaries, we can use ** because it takes all the argumnts of the dictionary inside it and compare them.
#cases that can be thought of:-
#1) This is the general case, query occurring in middle of the cards.
#2) Query is the first element.
#3) Query is the last element.
#4) The list contain just one element, that is the query itself.
#5) Cards does not contain the queried element.
#6) The list cards is empty.
#7) The list contains repeating numbers.
#8) The number query occurs at more than one position in cards.
# 5 and 6 are the edge cases because they occur in minimum(rare or extreme) cases.

#def func(a,b):
 #   if (b==0):
  #      return a
   # else:
    #    return func(b, a%b)
#ans = func(100, 2000)
#print(ans)

def locate_card(query, cards):
    low = 0
    high = len(cards)-1
    while low<=high:
        mid = (low+high)//2
        mid_number = cards[mid]

    
        if mid_number==query:
            return mid
        elif mid_number<query:
             high = mid-1
        else:
            low = mid +1

    return -1


#one more function should be added to the binary search program because, for instance, say that, a lost is given i decreasing order, and the query along with existing at the middle, may exist before the mid_number. Therefore, the exact position of the query must be the very first position of the queried number.
def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1>=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number< query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    low = 0
    high = len(cards) -1
    while low<=high:
        mid = (low+high)//2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            high = mid-1
        else:
            low = mid+1
    return -1


#Or
def binary_search(low, high, condition):
    while(low<=high):
        mid = (low+high)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid-1
        elif result == 'right':
            low = mid+1
    return -1


#Writing function inside a function which is called as function closure.
def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid>0 and cards[mid-1]==query:
                return 'left' #checks if there are any previous occurrences of the queried number
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(cards-1), condition)


#Now for example, say that the array is in increasing order and we need to find the starting and ending position of the queried number if it occurs for more than one time in the list.
#for that, we need to create two functions, first function will tell the first occurrence or the first position or the first index of the queried number, and the second function will tell the last occurrene of the querieed number.
def first_position(nums, target):
     def condition(mid):
        if nums[mid] == target:
            if mid>0 and nums[mid-1]==target:
                return 'left' 
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
     return binary_search(0, len(nums-1), condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid<len(nums)-1 and nums[mid+1]==target:
                return 'right' 
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums-1), condition)

