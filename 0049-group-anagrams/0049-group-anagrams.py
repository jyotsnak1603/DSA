from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char) - ord('a')] += 1
            anagram_map[tuple(count)].append(string)
        return list(anagram_map.values())