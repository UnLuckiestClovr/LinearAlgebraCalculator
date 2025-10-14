import numpy as np

from models.matrix import Matrix

def iterative_addition(matrices: list):
    matrixArray = np.array(matrices)

    result = None
    for matrixIndex in range(matrixArray.size):
        if result is None:
            print('Starting Addition...')
            result = Matrix(matrixArray[matrixIndex])
        else:
            if (result.data.shape != matrixArray[matrixIndex].shape):
                print("Matrices must have the same dimensions for addition.")
                break
            print(f'Adding \n{result} + \n{matrixArray[matrixIndex]}')

            # Show the addition step by step
            for i in range(result.shape[0]):
                rowStr = ""
                for j in range(result.shape[1]):
                    rowStr += f'{result.data[i][j]} + {matrixArray[matrixIndex][i][j]} = {result.data[i][j] + matrixArray[matrixIndex][i][j]} | '
                print(rowStr[:-3])  # Remove the last ' | ' for cleaner output

            result.add(matrixArray[matrixIndex])
            print(f'Result: \n{result.return_matrix()}')
    
    return result