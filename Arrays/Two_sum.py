class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        l2 = []
            
        for i in range(0, len(nums)):
            if nums[i] not in d:
                d[target-nums[i]] = i
            else:
                l2.append(i)
                l2.append(d[nums[i]])
                return l2
        return l2