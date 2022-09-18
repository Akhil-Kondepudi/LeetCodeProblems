class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = dict()
        for x in nums:
            if x in d:
                return True
            d[x] = True
        return False