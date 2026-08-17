class Solution(object):
    def characterReplacement(self, s, k):
        L=0
        
        freq={}
        max_freq=0
        answer=0
        
        for R in range(len(s)):
            freq[s[R]] =freq.get(s[R],0)+1

            max_freq=max(max_freq,freq[s[R]])

            while (R-L+1) -max_freq >k:
                freq[s[L]] -=1
                L+=1

            answer=max(answer,R-L+1)
        return answer

        


      