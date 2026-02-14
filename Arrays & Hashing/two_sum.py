"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""

# high complexity
def solution_1(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i]+nums[j]==target:
                return[i,j]
    return None

# O(n) complexity
def solution_2(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i
    return None
print(solution_2([2,1,3,8,3,7],6))