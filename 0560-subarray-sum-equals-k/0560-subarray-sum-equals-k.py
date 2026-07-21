class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        current_sum =0
        prefix_sums={0:1}

        for num in nums:
            current_sum += num
            difference = current_sum-k

            if difference in prefix_sums:
                count += prefix_sums[difference]
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) +1
        return count