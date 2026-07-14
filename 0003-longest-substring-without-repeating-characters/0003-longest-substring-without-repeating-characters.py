class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left=0
        maxlen=0
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left =char_map[char]+1
            char_map[char] = right
            maxlen = max(maxlen, right-left+1)
        return maxlen