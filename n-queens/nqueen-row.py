
from colors import Colors
def get_valid_input():
    """Get and validate user input for board size"""
    while True:
        try:
            n = int(input(f"{Colors.CYAN}Enter the number of queens (n): {Colors.END}"))
            if n <= 0:
                print(f"{Colors.RED}Please enter a positive integer.{Colors.END}")
                continue
            elif n == 1:
                print(f"{Colors.GREEN}Trivial case: 1 queen has 1 solution.{Colors.END}")
            elif n in [2, 3]:
                print(f"{Colors.YELLOW}No solutions exist for n={n}.{Colors.END}")
            return n
        except ValueError:
            print(f"{Colors.RED}Invalid input! Please enter a valid integer.{Colors.END}")

def solve_n_queens(n):
    """Solve the N-Queens problem and return all solutions"""
    solutions = []
    board = [-1] * n  # board[i] represents column position of queen in row i
    
    def is_safe(row, col):
        for i in range(row):
            # 1. Column Check:  board[i] == col
            # 2. Top left to bottom left (↘):       board[i] - i == col - row
            # 3. Top-right to bottom-left (↙):      board[i] + i == col + row

            # i means row iterator, board[i] gives col of queen placed in that row
            # col, and row variables are those in which we want to place the new queen

            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def placeQueens(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col            # record the col of queen for this row
                placeQueens(row + 1)        # move to next row
                board[row] = -1             # backtrack
    
    placeQueens(0)          # start from the first row
    return solutions

def display_solutions(solutions, n):
    if not solutions:
        print(f"{Colors.RED}No solutions found for n={n}!{Colors.END}")
        return
    
    print(f"{Colors.YELLOW}\n{'='*50}")
    print(f"    SOLUTION BOARDS FOR {n}-QUEENS")
    print(f"{'='*50}{Colors.END}\n")
    
    for idx, solution in enumerate(solutions, 1):
        print(f"{Colors.MAGENTA}Solution {idx}:{Colors.END}")
        
        for row in range(n):
            for col in range(n):
                if solution[row] == col:
                    print(f"{Colors.BOLD}{Colors.BLUE}Q {Colors.END}", end="")
                else:
                    print(f"{Colors.DARK_GRAY}. {Colors.END}", end="")
            print()
        print()
        
        # Interactive pause for large number of solutions
        if len(solutions) > 5 and idx % 3 == 0 and idx < len(solutions):
            input(f"{Colors.GREEN}Press Enter to see more solutions...{Colors.END}")

def main():
    print(f"{Colors.BOLD}{Colors.GREEN}🌟 N-Queens Problem Solver 🌟{Colors.END}")
    print(f"{Colors.CYAN}Find all possible arrangements of N queens on an NxN chessboard{Colors.END}\n")
    
    # Get input from the user
    n = get_valid_input()
    
    print(f"\n{Colors.BOLD}Total Queens: {n}{Colors.END}")
    print(f"{Colors.YELLOW}Solving... Please wait...{Colors.END}")
    
    # Call the solver
    solutions = solve_n_queens(n)
    
    # Display the solutions
    display_solutions(solutions, n)
    
    print(f"{Colors.BOLD}{Colors.GREEN}Total Solutions Found: {len(solutions)}{Colors.END}")
    
    # Ask if user wants to try again
    while True:
        again = input(f"\n{Colors.CYAN}Would you like to try another value? (y/n): {Colors.END}").lower()
        if again in ['y', 'yes']:
            print("\n" + "="*50)
            main()
            break
        elif again in ['n', 'no']:
            print(f"{Colors.BOLD}{Colors.BLUE}Thank you for using N-Queens solver! 👋{Colors.END}")
            break
        else:
            print(f"{Colors.RED}Please enter 'y' for yes or 'n' for no.{Colors.END}")

if __name__ == "__main__":
    main()