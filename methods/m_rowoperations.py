import numpy as np

from models.matrix import Matrix


def solve_matrix_values(matrixList: np.ndarray):
    """
    Perform row operations on a given matrix.
    Args:
        matrixList (list): A 2D list representing the matrix.
    """

    valueMatrix = matrixList[:, -1]
    coefficientMatrix = matrixList[:, :-1]  

    print(f'Value Matrix: \n{valueMatrix}')
    print(f'Coefficient Matrix: \n{coefficientMatrix}')

    matrix = Matrix(valueMatrix)

    matrix.print_matrix()
    solutions = matrix.solve_variables(coefficientMatrix)

    print(f'Solutions: {solutions}')