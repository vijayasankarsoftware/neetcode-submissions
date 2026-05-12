class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {')':'(', ']':'[', '}':'{'}

        stack = []

        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if not stack or stack.pop() != mapping[char]:
                    return False
        return True if not stack else False