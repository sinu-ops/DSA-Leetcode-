class Solution(object):
    def maxVowels(self, s, k):
        left=0
        n=len(s)
        count=0
        ans=0
        for i in range(k):
            if s[i] in "aeiou":
                count +=1
            ans=count

        for i in range(k,n):
            if s[i] in "aeiou":
                count +=1
                

            if s[left] in "aeiou":
                count -=1

            ans=max(ans,count)

            left +=1
        return ans
        


        


                
        

             
        
        