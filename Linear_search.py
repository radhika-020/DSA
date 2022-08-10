from turtle import position


def locate_card(cards, query):
    position = 0 #create a variable position with inital value 0

    while True: #A loop for repetition
        if cards[position] == query: #Check if the current position is the query
            return position # if yes, then answer found, return the position found.
        position = position+1 #ellse, increment the position by 1, till the queried number is not found at the position.

        if position == len(cards): # if the length of the cards exceeds, then return -1, check if you have reached the end of the cards
            return -1


#OR
def locate_card(cards, query):
    position= 0
    while position< len(cards):
        if cards[position] == query:
            return position # if yes, then answer found, return the position found.
        position = position+1 
    return -1
