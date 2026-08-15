class Solution(object):
    def strStr(self, haystack, needle):
        n=len(haystack) -len(needle) +1
        for i in range(n):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
           

       
            


        