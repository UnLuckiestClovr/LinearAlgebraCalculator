def matrix_addition(A: list,B: list):
    """
    Adds two matrices A and B of the same dimensions.

    Args:
        A (list): First matrix.
        B (list): Second matrix.
    """

    if (len(A) != len(B) or len(A[0]) != len(B[0])):
        # Throw an Error if either scale of the matrices (rows or columns) do not match exactly.
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    print(f'{A} + {B} = {[[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]}')
    
    return [
        # Iterates through the rows and columns of the matrices, adding corresponding elements.
        [A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))
    ]

