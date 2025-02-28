class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # buyprice = prices[0]
    # profit = 0

    # for sellprice in prices[1:]:
    #   if sellprice < buyprice:
    #     buyprice = sellprice
          
    #   profit = max(profit, sellprice - buyprice)

    # return profit


    # lowest = prices[0]
    # lowestidx = 0

    # for i in range(len(prices)):
    #   if prices[i] < lowest:
    #     lowest = prices[i]
    #     lowestidx = i

    # for i in range(lowestidx, len(prices)):

    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
      if prices[left] < prices[right]:
        curprof = prices[right] - prices[left]
        max_profit = max(curprof, max_profit)
      else:
        left = right
      right += 1

    return max_profit