class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort( key= lambda intervals: intervals[1])
        intervals.sort( key= lambda intervals: intervals[0])
        
        n = len(intervals)
        
        if n<2:
            return intervals
        
        i,j = 0,1
        cur = intervals[0]
        l1 = []
        
        while i<n and j<n:
            if intervals[j][0]<=cur[1]:
                cur = [cur[0], max(cur[1], intervals[j][1])]
            else:
                l1.append(cur)
                i = j
                cur = intervals[j]
            
            if(j<n-1):
                j+=1
            else:
                l1.append(cur)
                return l1
            
            
        
        return l1