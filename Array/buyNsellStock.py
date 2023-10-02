# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


#Buy low and sell high

####    Sliding Window
'''

def maxProfit(prices):
    left =0
    profit =0
    for right in range(1, len(prices)):
        if prices[left] < prices[right]:
            profit = max(profit, prices[right]-prices[left])
        else:
            left = right
    return profit


   

if __name__ == "__main__":
    # prices = [7,6,4,3,1]
    prices = [7,1,5,6,4]
    result = maxProfit(prices)
    print(result)
'''

#### Greedy approach

def maxProfit(prices):
    # Declare a buy variable, and max_profit variable
    # Initilize a buy variable to the first element of the prices array
    buy = prices[0]
    max_profit = 0
    # Iterate over the prices array and check if the current price is minimum or not
    for i in range(1, len(prices)):
        # If the current price is minimum then buy on this ith day.
        if (buy > prices[i]): 
            buy = prices[i]
        # If the current price is greater than the previous buy then make profit from it and maximize the max_profit
        elif (prices[i]-buy > max_profit):
            max_profit = prices[i] - buy
    return max_profit



if __name__=="__main__":
    prices = [7,1,5,6,4]
    max_profit = maxProfit(prices)
    print(max_profit)