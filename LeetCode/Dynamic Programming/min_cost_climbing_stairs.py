
def minCostClimbingStairs(cost) -> int:
    f1 = cost[0]
    f2 = cost[1]

    for i in range(2, len(cost)):
        current_cost = cost[i] + min(f1, f2)
        f1 = f2
        f2 = current_cost

    return min(f1, f2)
