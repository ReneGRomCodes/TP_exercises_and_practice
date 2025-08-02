# 1. Write a function that draws a grid like the following:

# +----+----+
# |    |    |
# |    |    |
# |    |    |
# |    |    |
# +----+----+
# |    |    |
# |    |    |
# |    |    |
# |    |    |
# +----+----+

def draw_grid():
    horizontal_row = "+----+----+"
    vertical_row = "|    |    |"
    print(2 * (horizontal_row + "\n" + 4 * (vertical_row + "\n")) + horizontal_row)


# 2. Write a function that draws a similar grid with four rows and four columns.

def draw_grid_four():
    horizontal_row = "+----+----+----+----+"
    vertical_row = "|    |    |    |    |"
    print(4 * (horizontal_row + "\n" + 4 * (vertical_row + "\n")) + horizontal_row)


# Alternative solution, letting the user chose the number of rows and columns.

def draw_grid_alt():
    """Take user input 'n_rows' and 'n_columns' to build a grid."""
    n_rows = int(input("Enter number of rows: "))
    n_columns = int(input("Enter number of columns: "))
    # Build horizontal and vertical lines.
    horizontal_row = "+----" * n_columns + "+"
    vertical_row = "|    " * n_columns + "|"
    # Build and print the grid.
    grid = (horizontal_row + "\n" + 4 * (vertical_row + "\n")) * n_rows + horizontal_row
    print(grid)
