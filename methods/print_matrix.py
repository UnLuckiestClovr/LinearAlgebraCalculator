def print_m(matrix: list):
    """
    Prints the matrix in a readable format.

    Args:
        matrix (list): The matrix to be printed.
    """
    for row in matrix:
        outputstr = ""
        for val in row:
            outputstr += f'{val} | '
        print(outputstr[:-3])  # Remove the last ' | ' for cleaner output

        print()  # Print a newline for better readability