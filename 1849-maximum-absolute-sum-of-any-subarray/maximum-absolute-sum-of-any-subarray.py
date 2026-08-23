class Solution(object):
    def maxAbsoluteSum(self, nums):
        curr_max=nums[0]
        curr_min=nums[0]
        abs_sum=abs(nums[0])
        for i in range(1,len(nums)):
            curr_max=max(curr_max+nums[i],nums[i])
            curr_min=min(curr_min+nums[i],nums[i])
            abs_sum=max(abs_sum,abs(curr_max),abs(curr_min))
        return abs_sum
            

        



      
        