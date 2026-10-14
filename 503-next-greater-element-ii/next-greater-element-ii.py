class Solution(object):
    def nextGreaterElements(self, nums):
        stack=[]
        n=len(nums)
        res=[-1] * n

        for i in range(n*2):
            index=i%n

            while stack and nums[stack[-1]] < nums[index]:
                j=stack.pop()
                res[j]=nums[index]
            
            if i < n :
                stack.append(index)
        return res


        
            


        
        