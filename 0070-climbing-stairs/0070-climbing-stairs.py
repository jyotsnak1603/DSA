class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        first,sec=1,2

        for i in range(3,n+1):
            current=first+sec
            first=sec
            sec=current
        return sec