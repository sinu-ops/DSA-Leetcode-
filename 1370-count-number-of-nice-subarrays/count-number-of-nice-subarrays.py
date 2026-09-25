class Solution(object):
    def numberOfSubarrays(self, nums, k):
        res=0
        prefix={0:1}
        curr_sum=0
        for num in nums:
            if num % 2 == 1:
              curr_sum += 1
            if curr_sum -k in prefix:
                res += prefix[curr_sum-k]
            prefix[curr_sum] = prefix.get(curr_sum,0)+1
        return res
                


        
        