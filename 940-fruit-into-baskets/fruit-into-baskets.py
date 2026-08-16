class Solution(object):
    def totalFruit(self, fruits):
        freq={}
        left=0
        max_len=0
        for R in range(len(fruits)):
            fruit=fruits[R]
            freq[fruit]=freq.get(fruit,0)+1


            while len(freq) >2:
                freq[fruits[left]] -=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left +=1

            max_len =max(max_len,R-left+1)
        return max_len
           






        
        

            

 


        

        
        



        
       
        