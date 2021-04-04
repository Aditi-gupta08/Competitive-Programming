class Solution:
    def search(self, nums: List[int], target: int) -> int:
           
        if not nums:
            return -1
        
        low = 0
        high = len(nums)-1
        
        
        while low<=high:
            mid = (low+high)//2
            
            if target<nums[mid]:
                if target<nums[low] and nums[low]<=nums[mid]:
                    low = mid +1
                else:
                    high = mid -1

            elif target>nums[mid]:
                if target>nums[high] and nums[high]>nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
                
            else:
                return mid
            
        return -1