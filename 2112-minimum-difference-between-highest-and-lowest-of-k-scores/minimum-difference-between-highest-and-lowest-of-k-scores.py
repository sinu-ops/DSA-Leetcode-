class Solution(object):
    def minimumDifference(self, nums, k):
        L=0
        diff=0
        res=float("inf")
        nums.sort()
        for R in range(len(nums)):
            if R-L+1 ==k:
                diff=nums[R] - nums[L]
                res=min(res,diff)
                L+=1
            
        return res



        

                
            


            
        
        