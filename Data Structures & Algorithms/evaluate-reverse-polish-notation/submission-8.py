class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                if token == '/':
                    stack.append(str(int(eval(f'{a}/{b}'))))
                    continue
                stack.append(eval(f'{a}{token}{b}'))
            else:
                stack.append(token)
        return int(stack[-1])