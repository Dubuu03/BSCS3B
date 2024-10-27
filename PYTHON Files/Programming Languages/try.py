
import sys

def minCoins(coins, m, V):
    # base case
    if (V == 0):
        return 0

    res = sys.maxsize

    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V - coins[i])


            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
    return res

coins = [20, 10, 5, 1]
m = len(coins)
V= int(input("Enter amount of change: "))
print("change("+str(V)+") = ", minCoins(coins, m, V))
