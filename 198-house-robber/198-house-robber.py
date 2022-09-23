class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        mem = {}
        def dfs(root):
            if root >= len(nums):
                return 0
            elif root in mem:
                return mem[root]
            else:
                curr = nums[root]
                out = max(curr + dfs(root + 2), curr + dfs(root + 3))
                mem[root] = out
                return out
        return max(dfs(0), dfs(1))