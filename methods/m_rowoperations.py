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


def find_matrix_determinant(matrixList: np.ndarray):
    """
    Find the determinant of a given matrix.
    Args:
        matrixList (list): A 2D list representing the matrix.
    """

    if (matrixList.shape[0] != matrixList.shape[1]):
        print("Determinant can only be calculated for square matrices.")
        return None
    if (matrixList.shape[0] == 1):
        return matrixList[0][0]


    # Formula : det(A) = Σ (−1)^i+j * a_ij * det(M_ij)

    numbers = []

    for row_num in range(matrixList.shape[0]):
        for column_num in range(matrixList.shape[1]):
            minor = np.delete(np.delete(matrixList, row_num, axis=0), column_num, axis=1)

            print(f'Calculating minor for element ({row_num}, {column_num}):'
                    f'\nElement Value: {matrixList[row_num][column_num]}'
                    f'\nMinor Matrix:\n{minor}')
            
            minor_determinant = find_matrix_determinant(minor)

            cofactor = ((-1) ** (row_num + column_num)) * matrixList[row_num][column_num] * minor_determinant
            numbers.append(cofactor)
            print(f'Cofactor for element ({row_num}, {column_num}): {cofactor}\n')
    determinant = 0
    for num in numbers:
        determinant += num

    print(f'Determinant: {determinant}')
    return determinant