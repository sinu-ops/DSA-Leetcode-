class Solution(object):
    def longestOnes(self, nums, k):
        zero_count=0
        max_win=0
        L= 0
        for R in range(len(nums)):
            if nums[R] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[L]==0:
                    zero_count-=1
                L += 1
            w=R-L+1
            max_win=max(w,max_win)
        return max_win

                
           
            
         
      

           
                
                    


        


        
        