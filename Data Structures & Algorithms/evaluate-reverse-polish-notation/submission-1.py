class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        numbers = list(range(-100,101))
        stack = deque()
        #edge cases - if tokens is empty
        

        #actual algorithm
        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack.popleft()
                

        
        


        


