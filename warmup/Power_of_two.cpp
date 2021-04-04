class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n<=0)
            return false;
        
        while(!(n%2)){
            n/=2;
        }
        
        if(n==1)
            return true;
        else
            return false;
    }
};