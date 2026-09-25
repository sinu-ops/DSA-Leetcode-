class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix={0:1}
        curr_sum=0
        res=0
        for num in nums:
            curr_sum += num
            if curr_sum - goal in prefix :
                res += prefix[curr_sum - goal]
            prefix[curr_sum] = prefix.get(curr_sum,0)+1
        return res




        
     
        