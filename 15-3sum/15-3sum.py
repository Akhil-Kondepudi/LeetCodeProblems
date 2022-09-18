class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        out = []
        seen = {}
        for x in range(len(nums)):
            if nums[x] > 0 or x == (len(nums) - 2):
                return out
            elif nums[x] not in seen:    
                first = x + 1
                last = len(nums) - 1
                while (first < last):
                    test = nums[x] + nums[first] + nums[last]
                    if (test == 0):
                        if [nums[x], nums[first], nums[last]] not in out:
                            out.append([nums[x], nums[first], nums[last]])
                    if test > 0:
                        last -= 1
                    else:
                        first += 1
                seen[nums[x]] = True
                    
            
    