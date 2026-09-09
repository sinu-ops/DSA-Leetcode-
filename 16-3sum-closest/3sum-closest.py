class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        left=0
        right=0
        curr_best=nums[0] +nums[1]+nums[2]
        for  i in range(n):
            if nums[i]>0 and nums[i] == nums[i-1]:
                continue
            left =i+1
            right =n-1
            while left < right :
                total=nums[i] + nums[left]+nums[right]
                if abs(total-target) <abs(curr_best-target):
                    curr_best =total
                if total <target :
                    left +=1
                elif total > target :
                    right -=1
                else:
                    return total 
        return curr_best
            


                



            


       
        