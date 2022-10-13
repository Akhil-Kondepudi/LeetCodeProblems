class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = 0
        while n:
            out += n % 2
            n = n >> 1
        return out