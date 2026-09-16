class Solution(object):
    def moveZeroes(self, nums):
        L=0
        for R in range(len(nums)):
            if nums[R] !=0:
                nums[L],nums[R]=nums[R],nums[L]
                L+=1
        return nums


        
      
            
      




      
        