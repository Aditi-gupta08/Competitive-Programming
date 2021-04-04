class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        if n<2:
            return 0
        
        intervals.sort(key = lambda intervals: intervals[1])
        i,j,cnt = 0,1,0
        
        while j<n:
            if intervals[i][1]>intervals[j][0]:
                    cnt+=1     
            else:
                i=j
            j+=1
            
            
        return cnt