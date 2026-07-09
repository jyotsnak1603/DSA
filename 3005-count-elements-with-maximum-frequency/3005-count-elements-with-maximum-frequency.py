from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = Counter(nums)

        max_freq = max(frequencies.values())

        return sum(f for f in frequencies.values() if f== max_freq)