class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for k in range(1, max(piles)+1):
        #     totaltime = 0
        #     for banana in piles:
        #         totaltime += math.ceil(banana/k)
            
        #     if totaltime<=h:
        #         return k
        # return max(piles)
        left, right = 1, max(piles)
        while left < right:
            mid = (left+right) //2
            totalhours = 0
            for banana in piles:
                totalhours += math.ceil(banana/mid)
            
            if totalhours <= h:
                right = mid
            else:
                left = mid+1
        return left