class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i.isdigit() or i[1::].isdigit():
                stack.append(int(i))
            else:
                if (i == "+"):
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first + second)
                elif (i == "-"):
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first - second)
                elif (i == "/"):
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first * 1.0 / second))
                elif (i == "*"):
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first * second)
        return(stack.pop())