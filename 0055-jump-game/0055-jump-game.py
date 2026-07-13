class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        n = len(nums)
        for i in range(0, n):
            if (i>maxReach):
                return False
            maxReach = max(maxReach, i+nums[i])

            if (maxReach >= n-1):
                return True