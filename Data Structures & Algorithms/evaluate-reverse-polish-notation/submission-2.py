class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    r = a + b
                elif t == "-":
                    r = a - b
                elif t == "*":
                    r = a * b
                elif t == "/":
                    r = int(a / b)

                stack.append(r)
        
        return stack[-1]


        [10, 6, -132]
        