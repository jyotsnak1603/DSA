class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length=0
        count=0

        indices={0:-1}

        for i,num in enumerate(nums):
            count += 1 if num==1 else -1

            if count in indices:
                max_length=max(max_length, i - indices[count])
            else:
                indices[count] = i
        return max_length