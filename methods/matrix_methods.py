import numpy as np

def iterative_addition(matrices: list):
    matrixArray = np.array(matrices)

    result = None
    for matrixIndex in range(matrixArray.size):
        if result is None:
            print('Starting Addition...')
            result = matrixArray[matrixIndex]
        else:
            if (result.shape != matrixArray[matrixIndex].shape):
                print("Matrices must have the same dimensions for addition.")
                break
            print(f'Adding {result} + {matrixArray[matrixIndex]}')
            result = result + matrixArray[matrixIndex]
            print(f'Result: {result}')
    
    return result


def matrix_addition(A: list,B: list):
    """
    Adds two matrices A and B of the same dimensions.

    Args:
        A (list): First matrix.
        B (list): Second matrix.
    """

    arrayA = np.array(A)
    arrayB = np.array(B)

    if (arrayA.shape != arrayB.shape):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = arrayA + arrayB

    print(f'{A} + {B} = {result}')

    return result