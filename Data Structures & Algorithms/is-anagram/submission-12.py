from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counted = Counter(s)
        t_counted = Counter(t)
        if not (s_counted == t_counted):
            return False
        return True