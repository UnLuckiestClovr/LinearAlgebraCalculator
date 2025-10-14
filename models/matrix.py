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
    
    def determinant(self):
        if self.data.shape[0] != self.data.shape[1]:
            raise ValueError("Determinant can only be calculated for square matrices.")
        return np.linalg.det(self.data)
    
    def solve_det(self):
        pass
    
    def return_matrix(self):
        return self.data