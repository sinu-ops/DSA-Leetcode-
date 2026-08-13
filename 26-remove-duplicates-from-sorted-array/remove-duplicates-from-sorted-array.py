class Solution(object):
    def removeDuplicates(self, nums):
        L=0
        n=len(nums)
        

        for R in range(1,n):
            if nums[R] != nums[L]:
                L+=1
                nums[L] =nums[R]
        return L+1
               
             
                
            
        
        
      
        