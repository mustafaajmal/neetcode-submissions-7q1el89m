class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ''.join(ch for ch in s if ch.isalnum()).lower()
        return filtered_string == filtered_string[::-1]