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


def iterative_subtraction(matrices: list):
    matrixArray = np.array(matrices)

    result = None
    for matrixIndex in range(matrixArray.size):
        if result is None:
            print('Starting Subtraction...')
            result = Matrix(matrixArray[matrixIndex])
        else:
            if (result.data.shape != matrixArray[matrixIndex].shape):
                print("Matrices must have the same dimensions for subtraction.")
                break
            print(f'Subtracting \n{result} - \n{matrixArray[matrixIndex]}')

            # Show the subtraction step by step
            for i in range(result.shape[0]):
                rowStr = ""
                for j in range(result.shape[1]):
                    rowStr += f'{result.data[i][j]} - {matrixArray[matrixIndex][i][j]} = {result.data[i][j] - matrixArray[matrixIndex][i][j]} | '
                print(rowStr[:-3])  # Remove the last ' | ' for cleaner output

            result.subtract(matrixArray[matrixIndex])
            print(f'Result: \n{result.return_matrix()}')

    return result

def iterative_matrix_multiplication(matrices: list):
    matrixArray = np.array(matrices)

    result = None
    for matrixIndex in range(matrixArray.size):
        if result is None:
            print('Starting Multiplication...')
            result = Matrix(matrixArray[matrixIndex])
        else:
            if (result.data.shape[1] != matrixArray[matrixIndex].shape[0]):
                print("Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.")
                break
            print(f'Multiplying \n{result} * \n{matrixArray[matrixIndex]}')

            # Show the multiplication step by step
            for i in range(result.shape[0]):
                rowStr = ""
                for j in range(matrixArray[matrixIndex].shape[1]):
                    cellSum = 0
                    cellStr = ""
                    for k in range(result.shape[1]):
                        cellSum += result.data[i][k] * matrixArray[matrixIndex][k][j]
                        cellStr += f'{result.data[i][k]}*{matrixArray[matrixIndex][k][j]} + '
                    cellStr = cellStr[:-3]  # Remove the last ' + ' for cleaner output
                    rowStr += f'Cell[{i},{j}]: {cellStr} = {cellSum} | '
                print(rowStr[:-3])  # Remove the last ' | ' for cleaner output

            result.multiply(matrixArray[matrixIndex])
            print(f'Result: \n{result.return_matrix()}')

    return result