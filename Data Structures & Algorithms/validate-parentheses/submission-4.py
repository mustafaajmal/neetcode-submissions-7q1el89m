class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in brackets:
                if stack:
                    top = stack.pop()
                    if not brackets[char] == top:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False