from collections import deque


# o(k * n) time o(k * n) space
def max_subarray_dp(A, k=1):
    maxes = dict()
    maxes[1] = A

    for i in range(2, k + 1):
        maxes[i] = list()
        for j in range(len(A) - i + 1):
            maxes[i].append(max(maxes[i - 1][j], A[j + i - 1]))

    return maxes[k]


# o(n) time o(k) space using a queue
def max_subarray(A, k=1):
    queue = deque()
    ans = []

    for i in range(k):
        queue.append(A[i])

    ans.append(max(queue))

    for i in range(k, len(A)):
        queue.popleft()
        queue.append(A[i])
        ans.append(max(queue))

    return ans


print(max_subarray_dp([1,2,3], 2))
print(max_subarray_dp([10,5,2,7,8,7], 3))

print(max_subarray([1,2,3], 2))
print(max_subarray([10,5,2,7,8,7], 3))
