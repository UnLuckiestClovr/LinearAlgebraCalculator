import numpy as np

from models.matrix import Matrix


def row_operations(matrixList:list):
    """
    Perform row operations on a given matrix.
    Args:
        matrixList (list): A 2D list representing the matrix.
    """

    matrix = Matrix(matrixList)

    matrix.print_matrix()

    return matrix.return_matrix()