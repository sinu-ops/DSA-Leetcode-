class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        if k == 0:
            return 1
        L=0
        bit_count=[0] *32
        min_len=float("inf")
        current_or=0
        for R in range(len(nums)):
            for b in range(32):
                if nums[R] & (1<<b):
                    bit_count[b] +=1
                    current_or |=(1<<b)
            while current_or >=k:
                min_len = min(min_len, R - L + 1)
                for b in range(32):
                    if nums[L] & (1 << b):
                        bit_count[b] -= 1
                        if bit_count[b] == 0:
                            current_or &= ~(1 << b)
                L += 1
        
        return -1 if min_len == float("inf") else min_len




      
        