class Solution(object):
    def pivotIndex(self, nums):
        total=sum(nums)
        left=0
        for i,num in enumerate(nums):
            right = total - left - num
            if left == right:
                return i
            left +=num
        return -1
        

        
        