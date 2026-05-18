class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = ["(", ")", "{", "}", "[", "]"]
        #always stack
        #when you encounter open paren, then you append to stack...
        stack = []
        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            if p == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            if p == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()

            if p == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        if stack:
            return False
        return True
                