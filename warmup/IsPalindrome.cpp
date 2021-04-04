class Solution {
public:
    bool isPalindrome(int x) {
        long long int p, s=0, r=0;
        p = x;
        
        if(x<0)
            return false;
        
        while(x>0)
        {
            r = x%10;
            s = s*10 +r;
            x/=10;
        }
        
        if(p==s)
            return true;
        else
            return false;
        
    }
};