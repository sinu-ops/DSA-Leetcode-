class Solution(object):
    def sortedSquares(self, nums):
        L=0
        R=len(nums) -1
        pos=len(nums)-1
        res=[0] *len(nums)
        while L<=R:
            if abs(nums[R]) > abs(nums[L]):
                res[pos]=nums[R] **2
                R-=1
            else:
                res[pos]=nums[L] **2
                L+=1

            pos -=1
        return res
    


      
        