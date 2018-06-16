"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.

This is a backtracking dynamic programming solution.

We need to explore the whole tree that is n_houses deep with a branching factor of n_colors:
O(n_colors ^ n_houses)

However, we will be able to prune already visited branches that we have determined a global minimum for.

This brings down the time complexity to:
O(n_houses * n_colors)

Why? The key is in the backtracking portion of this problem.

Once we select the global minimum of each house and color, we re-use those results for other minimums.

"""


def min_build_cost(n_houses, n_colors, cost):
    m = dict()

    def min_cost_dfs(house, color, current_cost):
        if (house, color) in m:
            return m[(house, color)]

        if house == n_houses:
            return current_cost

        min_cost = None
        for i in range(n_colors):
            if i == color:
                continue

            intermediate_cost = min_cost_dfs(house + 1, i, current_cost + cost[house][i])
            if min_cost is None or intermediate_cost < min_cost:
                min_cost = intermediate_cost

        m[(house, color)] = min_cost
        return min_cost

    return min_cost_dfs(0, 0, 0)


BUILD_COST = [
    [1, 2, 3],
    [1, 3, 5],
    [1, 2, -6],
    [1, 2, -8]
]

HOUSES = len(BUILD_COST)
COLORS = len(BUILD_COST[0])

print(min_build_cost(HOUSES, COLORS, BUILD_COST))