class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if(len(prices)<2):
            return 0
        
        mx_profit = 0
        mn_stock = prices[0]
        
        for i in range(1, len(prices)):
            mn_stock = min(mn_stock, prices[i])
            mx_profit = max(mx_profit, prices[i]-mn_stock)
            
        return mx_profit