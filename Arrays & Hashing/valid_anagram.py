"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""


# Not the best complexity
def solution_1(s,t):
    if len(s)!=len(t):
        return False
    if sorted(s)==sorted(t):
        return True
    else:
        return False

# better complexity with hashmap
def solution_2(s,t):
    hashmap_s= {}
    hashmap_t={}
    for elm in s:
        if elm not in hashmap_s.keys():
            hashmap_s[elm]=1
        else:
            hashmap_s[elm]+=1
    for elm in t:
        if elm not in hashmap_t.keys():
            hashmap_t[elm]=1
        else:
            hashmap_t[elm]+=1

    return (hashmap_t == hashmap_s)

print(solution_2("racecar","carrace"))