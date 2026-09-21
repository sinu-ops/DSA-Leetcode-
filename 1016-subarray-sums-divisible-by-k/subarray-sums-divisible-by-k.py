class Solution(object):
    def subarraysDivByK(self, nums, k):
        prefix={0:1}
        sum=0
        count=0
        reminder=0
        for num in nums:
            sum +=num
            reminder=sum % k
            if reminder in prefix:
                count += prefix[reminder]
            prefix[reminder]=prefix.get(reminder,0)+1
        return count

                
            
            
       
        