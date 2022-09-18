class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while(low <= high):
            curr = (high + low) / 2
            if target < nums[curr]:
                high = curr - 1
            elif target > nums[curr]:
                low = curr + 1
            else:
                return curr
        return -1
            
        
            