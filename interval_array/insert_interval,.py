class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if intervals==[]:
            return [newInterval]
        fl= -1
        k = 0
        i=0
        tmp = []
        n = len(intervals)
        
        if newInterval[1]<intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        
        while k==0 and i<n:
            
            if fl==-1:
                if intervals[i][1]>=newInterval[0]:
                    tmp = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                    fl = i
                    fl_2 = i+1
                elif i+1<n and intervals[i+1][0]>newInterval[1]:
                    intervals.insert(i+1, newInterval)
                    return intervals
                    
            else:
                if tmp[1]>=intervals[i][0]:
                    tmp[1] = max(tmp[1], intervals[i][1])
                    fl_2 += 1
                else:
                    del intervals[fl:fl_2]
                    intervals.insert(fl, tmp)
                    tmp=[]
                    k=1
                    
            i+=1
        if tmp!=[]:
            del intervals[fl:fl_2]
            intervals.insert(fl, tmp)
            
        if fl==-1:
            intervals.insert(i, newInterval)
        
        return intervals