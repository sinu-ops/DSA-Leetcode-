class Solution(object):
    def twoSum(self, numbers, target):
        L=0
        R=len(numbers) - 1
        curr_sum=0
        while L < R:
            curr_sum= numbers[L] + numbers[R] 
            if curr_sum > target:

                R-=1
            elif curr_sum < target:
                L+=1
            else:
                return [L+1,R+1]



    
        

       
        