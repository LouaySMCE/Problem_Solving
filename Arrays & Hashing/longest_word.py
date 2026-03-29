"""
Find the longest word in a sentence

Exemple: "Here we go again" -> "again"
Exemple: "Red Dead Redemption" -> "Redemption"
"""

def solution_1(s):
    M = []
    N = []
    t =""
    max_count = 0
    for i in range(len(s)):
        if s[i]!=" ":
            max_count += 1
        if s[i] == " " or i == len(s)-1:
            M.append(max_count)
            max_count = 0

    for elm in M:
        for j in range(elm):
            # not finished yet

print(solution_1("Red Dead Redemption Evolution"))