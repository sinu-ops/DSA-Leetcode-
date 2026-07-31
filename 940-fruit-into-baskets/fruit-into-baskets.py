class Solution(object):
    def totalFruit(self, fruits):
        count=collections.defaultdict(int)
        L=0
        total=0
        res=0
        for R in range(len(fruits)):
            count[fruits[R]] += 1
            total += 1
            while len(count) > 2:
                f=fruits[L]
                count[f] -= 1
                total -= 1
                L +=1

                if not count[f]:
                    count.pop(f)
            res=max(total,res)
        return res



        

        
        



        
       
        