class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        l = len(nums)
        if l==1:
            return nums[0]
        
        mx = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        
        for i in range(1, l):
            a = max_prod*nums[i]
            b = min_prod*nums[i]
            
            max_prod = max(a, b, nums[i])
            min_prod = min(a, b, nums[i])
            mx = max(mx, max_prod)
            
        return mx