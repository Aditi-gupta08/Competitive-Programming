class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if(len(nums)==0):
            return 0
        
        mx= nums[0]
        mx_till_now = 0
        
        for i in range(0, len(nums)):
            mx_till_now= max(nums[i], mx_till_now+nums[i])
            
            if(mx_till_now>mx):
                mx = mx_till_now
                
        return mx