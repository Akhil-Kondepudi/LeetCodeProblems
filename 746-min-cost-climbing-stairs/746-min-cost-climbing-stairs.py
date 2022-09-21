class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        mem = {}
        def dfs(root):
            if root > len(cost):
                return sys.maxint
            elif root == len(cost):
                return 0
            elif root in mem:
                return mem[root]
            else:
                out = min(dfs(root + 1), dfs(root + 2))
                mem[root] =  cost[root] + out
                return cost[root] + out
        return min(dfs(0), dfs(1))