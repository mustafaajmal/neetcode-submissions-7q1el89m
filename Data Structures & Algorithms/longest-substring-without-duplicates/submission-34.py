class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest_substring = 0
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)
        return longest_substring
        