class Solution(object):
    def moveZeroes(self, nums):
        new=0
        L=0
        for R in range(len(nums)):
            if nums[R]:
                nums[L],nums[R] = nums[R],nums[L]
                L +=1
        return nums




      
        