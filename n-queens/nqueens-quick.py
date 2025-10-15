"""Solve N-Queens problem and return all solutions"""
def solve_n_queens(n):
    solutions = []
    board = [-1] * n  # board[i] = row position of queen in column i
    
    """Check if placing queen at (col, row) is safe"""
    def is_safe(col, row):
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True
    
    def placeQueens(col):
        """Place queens column by column"""
        if col == n:
            solutions.append(board[:])
            return
        
        for row in range(n):
            if is_safe(col, row):
                board[col] = row
                placeQueens(col + 1)
                board[col] = -1
    
    placeQueens(0)
    return solutions


def print_board(solution, n):
    """Print a single solution board"""
    for row in range(n):
        for col in range(n):
            print('Q' if solution[col] == row else '.', end=' ')
        print()
    print()


def main():
    n = int(input("Enter n: "))
    solutions = solve_n_queens(n)
    
    print(f"\nTotal solutions: {len(solutions)}\n")
    
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        print_board(solution, n)


if __name__ == "__main__":
    main()