class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    MAGENTA = '\033[35m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    DARK_GRAY = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'  # Reset to default

# Usage
# print(Colors.RED + "This is red text" + Colors.END)
# print(Colors.GREEN + "This is green text" + Colors.END)
# print(Colors.BOLD + Colors.BLUE + "This is bold blue text" + Colors.END)