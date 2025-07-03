def maxProfit(prices) -> int:
    buy, sell = 0, 1
    maxProfit = 0
    
    while sell < len(prices):
        print(f"maxProfit, prices[buy], prices[sell] {maxProfit, prices[buy],prices[sell] }" )
        if prices[buy] > prices[sell]:
            buy = sell
        else:
            if (prices[sell] - prices[buy]) > maxProfit:
                maxProfit = prices[sell] - prices[buy]
        sell += 1
    return maxProfit

if __name__ == '__main__':
    # s = [4,2,0,3,2,5]
    # s = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = [2,1,2,1,0,1,2]


    print(maxProfit(s))