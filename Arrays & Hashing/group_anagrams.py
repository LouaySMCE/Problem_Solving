"""
Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""
import string
from valid_anagram import solution_2 as are_anagrams

alphabet = list(string.ascii_lowercase)

def solution(strs):
    L =[[strs[0]]]
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(1,len(strs)):
                if are_anagrams(strs[k],L[i][j]) :
                    L[i].append(strs[k])
                else:
                    L.append([strs[k]])
    return L
print(solution(["act","pots","tops","cat","stop","hat"]))