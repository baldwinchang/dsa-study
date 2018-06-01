def probability_of_knight_on_board_after_n_moves(r, c, n, moves):
    def on_board(r, c):
        return 0 <= r < n and 0 <= c < n

    def backtrack(r, c, moves_left):
        if not on_board(r, c):
            return 0
        if moves_left == 0:
            return 1 if on_board(r, c) else 0

        accumulator = 0.0
        for dr, dc in [[1, 3], [1, -3], [-1, -3], [-1, 3], [3, 1], [3, -1], [-3, -1], [-3, 1]]:
            accumulator += backtrack(r + dr, c + dc, moves_left - 1)
        return accumulator / 8

    return backtrack(r, c, moves)


print(probability_of_knight_on_board_after_n_moves(4, 4, 8, 1))
