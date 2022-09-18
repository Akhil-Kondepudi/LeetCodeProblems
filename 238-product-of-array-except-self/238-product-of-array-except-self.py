class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = list(nums)
        post = list(nums)
        curr = 1
        for x in range(len(pre)):
            pre[x] = curr * pre[x]
            curr = pre[x]
        curr = 1
        for x in range(len(post) - 1, -1, -1):
            post[x] = curr * post[x]
            curr = post[x]
        print(pre, post)
        for x in range(len(nums)):
            before = pre[x - 1] if x - 1 >= 0 else 1
            after = post[x + 1] if x + 1 < len(nums) else 1
            nums[x] = before * after
        return nums