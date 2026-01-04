prices = [180, 182, 179, 185]

returns = []
for i in range(1, len(prices)):
    returns.append((prices[i] - prices[i-1]) / prices[i-1])
print(returns)

