class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s = ''
        l = max(len(num1), len(num2))
        num1 = num1.zfill(l)
        num2 = num2.zfill(l)
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        r = 0
                
        for i in range(0, l):
            tmp = int(num1[i]) + int(num2[i]) + r
            if(tmp>9):
                tmp = str(tmp)
                r = int(tmp[0])
                s+= tmp[1]
            else:
                s+= str(tmp)
                r=0
            
                
        if(r>0):
            s+=str(r)
                
        s = s[::-1]
        return s
                
                
            