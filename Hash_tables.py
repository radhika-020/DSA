#Hash tables are used in python to create dicionaries with the key value pairs.
phone_numbers = {'Radhika' : '8887693624', 'Anjani': '9335344759', 'Ranjana': '9335972648'}
#we can either access the dictionary by:
for name in phone_numbers:
    print ('Name', name, 'Phone Number', phone_numbers[name])

#We can either acess the dictionary by declaring the dictionary by
max_hash_table_size = 4096
#at the first, all the keys in dictionaries are assigned with the value None, therefore,
hash_table = [4096]*None
#assert keyword is used to continue the loop till the assert condition is true, once it encounters a false condition, it throws an error.
#for loop is used to iterate over all the items of the hash_able created.
for item in hash_table:
    assert item == None #This statement will not throw an error as all the items are None, by default, at the initial stage.

#but
for item in hash_table:
    assert item == 7 #This statement will throw an error when the assert condition goes to false.

#A hashing function is usded to convert strings and other non-numeric data types into numbers, which can then be used as list indices. For instance, if a hashing function converts the string 'Radhika' into the number 4, then the key-value pair ('Radhika', '8887693624') will be stored at the position 4 within the list.
#An algorithm which converts strings into numeric list indices:-
#1) iterate over the string, character by character
#2) Conert each character to a number using Python's built in ord function.
#3) Add the numbers for each character to obtain the hash for the entire string.
#4) Take the reminder of the result with the size of the data list.

#A function to get an index of the full string.
def get_index(data_list, a_string):
    result = 0

    for a_character in a_string: #Loop is iterated character by character because the ord function can convert a character into a number and not full string at once.
        a_number = ord(a_character)
        result = result + a_number

    list_index = result % len(data_list) #We are dividing the result by our total length of the list because the result obtained can be of greater value, so by dividing and obtaining the remaimder from the length of the data list, it will give us a number within the range of our data list.
    return list_index


#List Compehension(used for performing complex operations on lists and dictionaries)
list1 = [1, 2, 3, 4, 5]
list2 = [x for x in list1] #will print the copy of list1
list3 = [x*x for x in list1] #will print [1, 4, 9, 16, 25]
#we can also import a function, like import math and perform operations accordingly. Say for instance,
import math
list4 = [1.3, 2.5, 3.2, 6, 7]
list5 = [math.ceil(x) for x in list4] #will print the ceiling of the numbers, i.e., [2, 3, 4, 6, 7] 
#List Comprehension can also be written with a if condition,
list6 = [math.ceil(x) for x in list4 if x>2] #will print ceiling of all the numbers from list4 that are greater than 2, i.e., [3, 4, 6, 7].
#To get the list of the keys, 
key_value = ('Radhika', 'Ranjana', 'Anjani')
keys = [key_value[0] for key_value in data_list if key_value is not None]

class BasicHashTable:
    def __init__(self, max_size = max_hash_table_size): #if we do not provide the max size of the list, then it will automaticalluy take 4096 elements, but if provided, then it will take the provided max size of the list.
    #creating a list of size 'max_size' with all values None
        self.data_list = [None]*max_size

    def insert(self, key, value):
        #Find the index for the key using get_index
        index = get_index(self.data_list, key)
        #Store the key-value pair at the right index.
        self.data_list[index]=(key, value)

    def find(self, key):
        #Find the index for key using get_index
        index = get_index(self.data_list, key)
        #Retrieve the data stored at the index
        key_value = self.data_list[index]
        #Return the value if found, else return None
        if key_value is None:
            return None
        else:
            key, value = key_value
            return value

    def update(self, key, value):
        #Find the index for the key using get_index
        index = get_index(self.data_list, key)
        #Store the ney key_value pair at the right index
        self.data_list[index] = key, value

    def list_all(self):
        #Extract the key from each key-value pair
        return [key_value[0] for key_value in self.data_list if key_value is not None]

basic_table = BasicHashTable(max_size=1024)
#we can check the length of the basic_table by len(basic_table) function.
basic_table.insert('Radhika Arora', '7398211236')


#There occurs a concept of Collision, in which, when two strings, which have the same set of characers or letters but in different order might occupy a same hash index. For example, listen and silent.
#To handle collisions, there occurs a concept of Linear Probing.
