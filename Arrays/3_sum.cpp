class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>>res;
        
        sort(nums.begin(), nums.end());
        
        if(n<3)
            return {};
        
        for(int i=0; i<n-2; i++)
        {
            if(i>0 && nums[i-1]==nums[i])
                continue;
            
            int l = i+1;
            int h = n-1;
            int t = -nums[i];
            
            while(l<h)
            {
                if(l>i+1 && nums[l-1]==nums[l])
                {
                    ++l;
                    continue;
                }
                    
                
                int add = nums[l]+nums[h];
                
                if(t==add)
                {
                    res.push_back({nums[i], nums[l], nums[h]});
                    l++;
                }
                else if(t<add)
                    --h;
                else
                    ++l;
            }
        }
        
        return res;
    }
};