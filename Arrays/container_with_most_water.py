class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        mx = 0
        
        while i<j:
            if height[i]<height[j]:
                mx = max(mx, (height[i])*(j-i))
                i+= 1
            else:
                mx = max(mx, (height[j])*(j-i))
                j-= 1

        return mx
                    