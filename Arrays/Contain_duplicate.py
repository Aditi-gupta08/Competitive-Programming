class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(1, len(nums)):
            if( nums[i-1] == nums[i]):
                return 1
        return 0