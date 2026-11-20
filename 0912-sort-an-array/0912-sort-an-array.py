class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def divide(num):
            if(len(num)<=1):
                return num
            mid=len(num)//2
            left=num[:mid]
            right=num[mid:]
            left=divide(left)
            right=divide(right)
            return merge(left,right)
        def merge(left,right):
            new=[]
            i=0
            j=0
            while(i<len(left) and j<len(right)):
                if(left[i]<right[j]):
                    new.append(left[i])
                    i+=1
                else:
                    new.append(right[j])
                    j+=1
            new.extend(left[i:])
            new.extend(right[j:])
            return new
        result=divide(nums)
        return result
        