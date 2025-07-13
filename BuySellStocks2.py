"""Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.
Input Format
9
310 315 275 260 270 290 230 255 250
"""
n = int(input())
prices = list(map(int,input().split()))
max_profit = 0
min_price = prices[0]
for i in range(len(prices)):
    if prices[i]< min_price:
        min_price = prices[i]
    profit = prices[i] - min_price
    max_profit = max(profit,max_profit)
print(max_profit)
  
