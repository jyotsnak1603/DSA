class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currentReach = 0
        maxReach = 0
        n=len(nums)
        for i in range(0,n-1):
            maxReach = max(maxReach, i+nums[i])
            if (i==currentReach):
                jumps += 1
                currentReach = maxReach
        return jumps