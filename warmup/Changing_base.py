class Solution:
    def baseNeg2(self, n: int) -> str:
        
        if n==0:
            return '0'
        
        s1 = ""
        
        while n!=0:
            s1+= str(n%2)
            n/=-2
            n = ceil(n)
        
        return s1[::-1]