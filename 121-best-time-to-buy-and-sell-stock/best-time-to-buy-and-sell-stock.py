class Solution(object):
    def maxProfit(self, prices):
        # using sliding window 
        l , r=0,1
        MaxP=0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit=prices[r] - prices[l]
                MaxP=max(MaxP,profit)
            else:
                l=r
            r +=1
        return MaxP
        
      
        