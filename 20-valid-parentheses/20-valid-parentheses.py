class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [];
        for x in s:
            if x == "(" or x == "{" or x == "[":
                stack.append(x);
            else:
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if out == "(" and x != ")":
                    return False
                if out == "{" and x != "}":
                    return False
                if out == "[" and x != "]":
                    return False
        if (len(stack) > 0):
            return False
        return True;