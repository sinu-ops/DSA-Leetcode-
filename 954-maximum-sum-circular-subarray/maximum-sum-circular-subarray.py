class Solution(object):
    def maxSubarraySumCircular(self, nums):
        curr_max=nums[0]
        best_max=nums[0]
        total_sum=nums[0]
        min_sum=nums[0]
        best_min=nums[0]

        for i in range(1,len(nums)):
            total_sum +=nums[i]
            curr_max=max(
                curr_max+nums[i],nums[i]
            )
            min_sum=min(min_sum+nums[i],nums[i])
            best_min=min(best_min,min_sum)

            best_max=max(
                curr_max,best_max
            )
        if best_max <0 :
            return best_max
        
        circular_sum=total_sum-best_min

        return max(circular_sum,best_max)

        



           
      



      
        