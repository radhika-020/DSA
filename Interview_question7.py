#To check whether two strings are anagrams or not. The strings are anagrams if they are made up of same characters with same frequency possibly in different order.


from collections import Counter

def strings(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    if counter1 == counter2:
        print("Anagrams")
    elif len(s1)!=len(s2):
        print("Not Anagrams.")
    else:
        print("Not Anagrams.")

#OR

def strings(s1, s2):
    if len(s1)!=len(s2):
        return False
    else:
        return sorted(s1) == sorted(s2)

#OR

def strings(s1, s2):
    if len(s1)!=len(s2):
        return False
    else:
        return Counter(s1) == Counter(s2)
