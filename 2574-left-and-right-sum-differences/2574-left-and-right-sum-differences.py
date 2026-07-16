class Solution(object):
    def leftRightDifference(self, nums):
        total_sum=sum(nums)
        left_sum=0
        a=[]
        for num in nums:
            total_sum-=num
            a.append(abs(left_sum-total_sum))
            left_sum +=num
        return a
        
        