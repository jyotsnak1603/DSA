class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m,n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            part1 = (low+high)//2
            part2 = (m+n+1) // 2-part1

            maxleft1 = float('-inf') if part1 == 0 else nums1[part1-1]
            minright1 = float('inf') if part1==m else nums1[part1]

            maxleft2 = float('-inf') if part2 == 0 else nums2[part2-1]
            minright2 = float('inf') if part2 == n else nums2[part2]

            if maxleft1 <= minright2 and maxleft2 <= minright1:
                if (m+n)%2 == 1:
                    return max(maxleft1, maxleft2)
                else:
                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2.0
            elif maxleft1>minright2:
                high=part1-1
            else:
                low=part1+1
        return 0.0