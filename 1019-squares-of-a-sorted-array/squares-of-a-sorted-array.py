class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        L=0
        R = n-1
        ans=[0] * n
        write= n-1
        while L <=R:
            if abs(nums[L]) > abs(nums[R]):
                ans[write] = nums[L] **2 
                L +=1
            else:
                abs(nums[L] ) < abs(nums[R])
                ans[write] = nums[R] **2
                R -=1
            write -=1
        return ans

                

            


        
                

       



        