class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_substring = 0
        local_max = 0
        if len(s) == 1:
            return 1
        while r <= len(s):
            if r == len(s):
                splice = s[l:r+1]
            else:
                splice = s[l:r]
            subset = set(splice)
            if len(splice) != len(subset):
                r += 1
                l += 1
            else:
                r += 1
                local_max += 1
                max_substring = max(max_substring, local_max)
            print(local_max)
            print(max_substring)
            print(splice)
            print(s[l:r+1])
            # print(subset)
        return max_substring
            
        