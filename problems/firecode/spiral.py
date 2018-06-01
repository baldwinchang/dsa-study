"""
Spiral Print

Analysis:

Runtime:
O(m * n) the main loop will run for all values within the matrix, doing O(1) work each

Space:
O(m * n) outside of O(1) constant space for tracking variables, we need to store all of the values in the matrix
"""


def find_spiral(matrix):
    m = len(matrix)
    n = len(matrix[0])

    m_bound = m
    n_bound = n

    r, c = 0, 0
    dr, dc = 0, 1

    spiral = []
    size = m * n
    while len(spiral) != size:
        spiral.append(matrix[r][c])

        if r == (m - m_bound) and c == (n_bound - 1) and dr == 0 and dc == 1:
            dc = 0
            dr = 1
        elif r == (m_bound - 1) and c == (n_bound - 1) and dr == 1 and dc == 0:
            dc = -1
            dr = 0
        elif r == (m_bound - 1) and c == (n - n_bound) and dr == 0 and dc == -1:
            m_bound -= 1
            dc = 0
            dr = -1
        elif r == (m - m_bound) and c == (n - n_bound) and dr == -1 and dc == 0:
            n_bound -= 1
            dc = 1
            dr = 0

        r += dr
        c += dc

    return spiral

print(find_spiral([[1, 2], [3, 4]]))