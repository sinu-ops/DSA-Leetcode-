class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res=[]
        start1=intervals[0][0]
        end1=intervals[0][1]
        for i in intervals:
            if i[0] <= end1:
                end1=max(end1,i[1])
            else:
                res.append([start1,end1])
                start1=i[0]
                end1=i[1]
        res.append([start1,end1])
        return res

        
            

       