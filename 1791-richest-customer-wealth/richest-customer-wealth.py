class Solution(object):
    def maximumWealth(self, accounts):
        res=0
        for customer in accounts:
            wealth=0

            for money in customer:
                wealth += money
                res=max(res,wealth)
                
                
        return res
        
        
            
        


        