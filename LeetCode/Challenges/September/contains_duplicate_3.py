class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False  # edge case

        seen = {}
        for i, x in enumerate(nums):
            bkt = x//(t+1)
            if bkt in seen and i - seen[bkt][0] <= k:
                return True
            if bkt-1 in seen and i - seen[bkt-1][0] <= k and abs(x - seen[bkt-1][1]) <= t:
                return True
            if bkt+1 in seen and i - seen[bkt+1][0] <= k and abs(x - seen[bkt+1][1]) <= t:
                return True
            seen[bkt] = (i, x)
        return False
