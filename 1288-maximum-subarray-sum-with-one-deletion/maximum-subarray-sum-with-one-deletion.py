class Solution(object):
    def maximumSum(self, arr):
        no_deletion=arr[0]
        one_deletion=arr[0]
        answer=arr[0]
        for i in range(1,len(arr)):
            new_no_deletion=max(arr[i],no_deletion + arr[i])

             
            new_one_deletion=max(one_deletion+arr[i],no_deletion)

            no_deletion=new_no_deletion
            one_deletion=new_one_deletion

            answer=max(no_deletion,one_deletion,answer)
        return answer
       
        