"""
Check if a string is a palindrome
A palindrome is a word that is the same forward and backward.
"radar" -> True , "level" -> False
"""

# An easy approach is using the same method in reverseF.py
def fst_function(s):
    L = []
    t = ""
    for i in range(len(s) - 1, -1, -1):
        L.append(s[i])
    for j in range(len(L)):
        t = t + L[j]
    return s==t

# A solution that I got immediately but has useless storing results
def snd_function(s):
    L = []
    for i in range(len(s)):
        if s[i] == s[-1-i]:
            L.append(True)
        else:
            L.append(False)
    if False in L:
        return False
    else:
        return True

# Improving the previous one
def thrd_function(s):
    for i in range(len(s)):
        if s[i] != s[-1-i]:
            return False
    return True

print(thrd_function("radar"))