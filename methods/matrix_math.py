import numpy as np


class Matrix:
    def __init__(self, data: list):
        self.data = np.array(data)

    def add(self, added_matrix:list):
        self.data = self.data + np.array(added_matrix)
        return self
    
    def subtract(self, subtracted_matrix:list):
        self.data = self.data - np.array(subtracted_matrix)
        return self
    
    def multiply(self, multiplied_matrix:list):
        self.data = self.data @ np.array(multiplied_matrix)
        return self
    
    def multify_scalar(self, scalar:float):
        self.data = self.data * scalar
        return self
    
    def divide_scalar(self, scalar:float):
        self.data = self.data / scalar
        return self

    
    def return_matrix(self):
        return self.data


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
            print(f'Adding \n{result} + \n{matrixArray[matrixIndex]}')

            # SHow the addition step by step
            for i in range(result.shape[0]):
                rowStr = ""
                for j in range(result.shape[1]):
                    rowStr += f'{result[i][j]} + {matrixArray[matrixIndex][i][j]} = {result[i][j] + matrixArray[matrixIndex][i][j]} | '
                print(rowStr[:-3])  # Remove the last ' | ' for cleaner output

            result = result + matrixArray[matrixIndex]
            print(f'Result: \n{result}')
    
    return result