class Solution(object):
    def minWindow(self, s, t):
        L=0
        need={}
        window={}
        have=0
        
        
        for R in range(len(t)):
            need[t[R]]=need.get(t[R],0)+1
        req=len(need)

        min_len=float("inf")
        answer=""

        for R in range(len(s)):
            if s[R] in need:
                window[s[R]]=window.get(s[R],0)+1
                if window[s[R]] == need[s[R]]:
                    have+=1
                    while have == req:
                        if R-L+1 < min_len:
                            min_len=R-L+1
                            answer=s[L:R+1]
                        if s[L] in need:
                            window[s[L]] -=1
            
                            if window[s[L]] < need[s[L]]:
                                have -=1
                        L+=1
        return answer


        
                    


                

            

            

        
        