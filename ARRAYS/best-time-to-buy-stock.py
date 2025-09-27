def maxProfit(prices):
    position = 0
    profit = 0
    while position < len(prices) - 1:              # stop at second-last index
        if prices[position] < prices[position + 1]:
            profit += prices[position + 1] - prices[position]
        position += 1                               # always move forward
    return profit


print(maxProfit([7,1,5,3,6,4])) 
print(maxProfit([1,2,3,4,5]))    
print(maxProfit([7,6,4,3,1]))   