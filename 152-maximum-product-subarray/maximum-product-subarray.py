class Solution(object):
    def maxProduct(self, nums):
        curr_max=nums[0]
        curr_min=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            prev_max=curr_max
            prev_min=curr_min
            curr_max=max(nums[i],prev_max*nums[i],prev_min *nums[i])
            curr_min=min(nums[i],prev_max*nums[i],prev_min *nums[i])
            res=max(res,curr_max,curr_min)

        return res
           



       
        