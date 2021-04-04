class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mul1 = []
        mul2 = []
        ans = 1
        res = []
        
        for i in range(0, len(nums)):
            mul1.append( ans)
            ans*= nums[i]
            
        ans= 1
        for i in range(len(nums)-1, -1, -1):
            mul2.append(ans)
            ans*= nums[i]
            
        mul2 = mul2[::-1]
            
        for i in range(0, len(nums)):
            res.append( (mul1[i])*(mul2[i]) )
       
        return res
            
        