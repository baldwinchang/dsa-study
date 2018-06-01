"""
 Topological Sort
 Time: O(|V| + |E|) linear complexity, we explore each (u, v) edge in a graph
 Space: O(|V|) we store each vertex as we complete the sort. Once in the visited set, once as the sorted order.

 Topological sort is useful as a way to order dependencies (tasks, requirements, etc).

 In the below example, imagine the classical example of getting ready to leave the house.
 Before you go to work, you have to put on clothes in a specific order.
 Maybe you have to brush your teeth prior to eating breakfast.

 Topological sort is a powerful algorithm for precisely this task.
"""

from collections import defaultdict, deque

"""
0 -> 1 ->  3
 \   | \
  \  v  \
   > 2   > 4
     |
     v
     5
"""
# Let G be an adjacency list, representing the above graph
G = defaultdict(list)
G[0] = [1, 2]
G[1] = [2, 3, 4]
G[2] = [5]
G[6] = []


def topological_sort(graph):
    visited = set()

    def visit(u):
        visited.add(u)
        for neighbor in graph[u]:
            if neighbor not in visited:
                visit(neighbor)
        sorted_order.appendleft(u)

    sorted_order = deque()
    for vertex in graph.keys():
        if vertex not in visited:
            visit(vertex)
    return [v for v in sorted_order]


print(topological_sort(G))