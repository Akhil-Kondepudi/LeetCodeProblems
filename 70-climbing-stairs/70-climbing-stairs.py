class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = {}
        
        def dfs(x):
            if x > n:
                return 0
            elif x == n:
                return 1
            elif x in mem:
                return mem[x]
            else:
                out = dfs(x + 1) + dfs(x + 2)
                mem[x] = out
                return out
        return dfs(0)