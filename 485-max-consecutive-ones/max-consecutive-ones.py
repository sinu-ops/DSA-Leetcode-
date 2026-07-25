class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_count=0
        L=0
        for R in range(len(nums)):
            if nums[R] == 1:
                count +=1
            else:
                count=0
            max_count=max(count,max_count)
        return max_count



           
       
        