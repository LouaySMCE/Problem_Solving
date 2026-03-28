"""
Find the first non-repeating character in a string

exemple : "aabbcdd" -> "c"
exemple : "hello" -> "h"

"""

def solution_1(s):
    hashmap ={}
    for i in range(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]] = 1
        else:
            hashmap[s[i]] += 1
    for elm in hashmap.keys():
        if hashmap[elm]==1:
            return elm
    return None


print(solution_1("aaabbbc"))
