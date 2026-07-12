class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] > prices[j]:
                    continue
                else:
                    if prices[j] - prices[i] > max_diff:
                        max_diff = prices[j] - prices[i]
        return max_diff
        