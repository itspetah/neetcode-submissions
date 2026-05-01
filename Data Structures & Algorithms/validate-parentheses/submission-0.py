class Solution:
    def isValid(self, s: str) -> bool:
        legend = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        
        for letter in s:
            if letter in legend:
                stack.append(letter)
            else:  
                if not stack or legend[stack.pop()] != letter:
                    return False
        
        return not stack
