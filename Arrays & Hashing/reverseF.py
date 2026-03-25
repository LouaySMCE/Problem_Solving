"""
Given a String s, reverse it without using native functions or slicing

exemple : reverseF("hello") = "olleh"
"""

def reverseF(s):
    L = []
    t = ""
    for i in range(len(s)-1, -1, -1):
        L.append(s[i])
    for j in range(len(L)):
        t = t + L[j]
    return t

print(reverseF("hello"))
