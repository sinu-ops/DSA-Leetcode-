class Solution(object):
    def minimumDifference(self, nums, k):
        L=0
        dif=0
        res=float("inf")
        nums.sort()
        for R in range(len(nums)):
            if R-L+1 ==k:
                dif=nums[R] - nums[L]
                res=min(res,dif)
                L+=1
            
        return res



        

                
            


            
        
        