# Question - https://leetcode.com/problems/contains-duplicate-ii/submissions/

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i, x in enumerate(nums): 
            if x in seen and i - seen[x] <= k: return True 
            seen[x] = i
        return False 