"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

# complexity O(n²)
def solution_1(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i]==nums[j]:
                return True
    return False

# complexity O(n²)
def solution_2(nums):
    L = []
    for elm in nums:
        if elm not in L:
            L.append(elm)
    return(not (L==nums))

#-------------complexity O(n)-----------------
def solution_optimized(nums):
    S = set()
    for elm in nums:
        if elm in S:
            return True
        else:
            S.add(elm)
    return False