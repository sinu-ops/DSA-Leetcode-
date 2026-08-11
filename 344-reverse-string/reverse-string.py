class Solution(object):
    def reverseString(self, s):
        L=0
        n=len(s)
        R=n-1
        while L<R:
            s[L],s[R]=s[R],s[L]
            L+=1
            R-=1


        


       
        