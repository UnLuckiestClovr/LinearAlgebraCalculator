import numpy as np


class Matrix:
    def __init__(self, data: list):
        self.data = np.array(data)

    def swap(self, row1:int, row2:int):
        row1Data = self.data[row1]
        self.data[row1] = self.data[row2]
        self.data[row2] = row1Data

        return self
    
    def scale(self, row:int, scalar:float):
        self.data[row] = self.data[row] * scalar
        return self
    
    def add_scaled(self, source_row:int, target_row:int, scalar:float):
        self.data[target_row] = self.data[target_row] + (self.data[source_row] * scalar)
        return self
    
    def subtract_scaled(self, source_row:int, target_row:int, scalar:float):
        self.data[target_row] = self.data[target_row] - (self.data[source_row] * scalar)
        return self
    
    def return_matrix(self):
        return self.data


def row_operations(matrixList:list):
    """
    Perform row operations on a given matrix.
    Args:
        matrixList (list): A 2D list representing the matrix.
    """

    matrix = Matrix(matrixList)



    return matrix.return_matrix()