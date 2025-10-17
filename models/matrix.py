import numpy as np
from fractions import Fraction


class Matrix:
    def __init__(self, data):
        if isinstance(data, list):
            self.data = np.array(data)
            self.shape = self.data.shape
        elif isinstance(data, np.ndarray):
            self.data = data
            self.shape = self.data.shape

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
    
    def add_number(self, number:float):
        self.data = self.data + number
        return self
    
    def subtract(self, subtracted_matrix:list):
        self.data = self.data - np.array(subtracted_matrix)
        return self
    
    def subtract_number(self, number:float):
        self.data = self.data - number
        return self
    
    def multiply(self, multiplied_matrix:list):
        self.data = self.data @ np.array(multiplied_matrix)
        return self
    
    def multiply_scalar(self, scalar:float):
        self.data = self.data * scalar
        return self
    
    def divide_scalar(self, scalar:float):
        self.data = self.data / scalar
        return self
    
    def determinant(self):
        if self.data.shape[0] != self.data.shape[1]:
            raise ValueError("Determinant can only be calculated for square matrices.")
        
        det = np.linalg.det(self.data)
        self.print_matrix()
        print(f'Determinant: {det}')

        return det

    def solve_variables(self, solution_matrix: np.ndarray):
        """
        Solve a system of linear equations using Cramer's Rule.
        To keep scalability high, we will not hardcode for 2x2 or 3x3 matrices, instead choosing to use a "Solution Array".

        Args:
            solution_matrix (list): A 1D list representing the constants on the right side of the equations.
        Returns:
            list: A list containing the solutions for each variable. [x: value, y: value, z: value, ...]
        """
        # Instead of hardcoding values we will store them in a list to allow for scalability.
        variableSolutions = []
            
        # Find the determinant of the original matrix
        D = self.determinant()
        for i in range(self.shape[0]):
            modified_matrix = Matrix(self.data.copy())

            # Replace the i-th column with the solution matrix
            for j in range(self.shape[1]):
                    modified_matrix.data[j][i] = solution_matrix[j]

            # Calculate the determinant of the modified matrix
            D_i = modified_matrix.determinant()

            # Calculate the value of the variable using Cramer's Rule
            variableSolutions.append(Fraction(D_i / D).limit_denominator().__str__() if D != 0 else 0)

        return variableSolutions
    

    def transpose(self):
        self.data = self.data.T
        return self

    def inverse(self):
        if (self.determinant() == 0):
            raise ValueError("Matrix is singular and cannot be inverted.")

        # Ensure the matrix is square
        num_rows, num_cols = self.shape
        if num_rows != num_cols:
            raise ValueError("Inverse can only be calculated for square matrices.")

        # Create an identity matrix of the same shape
        identity = np.eye(num_rows)
        augmented_matrix = np.hstack((self.data.copy(), identity))

        print(self.data)
        print("➡️ Starting Inversion Process (A | I) → (I | A⁻¹):")

        for pivot_row in range(num_rows):
            pivot_value = augmented_matrix[pivot_row, pivot_row]

            # Handle Possible Zero-Pivots
            if pivot_value == 0:
                for row in range(pivot_row + 1, num_rows):
                    if augmented_matrix[row, pivot_row] != 0:
                        augmented_matrix[[pivot_row, row]] = augmented_matrix[[row, pivot_row]]
                        break
                else:
                    raise ValueError("Matrix is singular and cannot be inverted.")
                
                pivot_value = augmented_matrix[pivot_row][pivot_row]
            
            # Normalize the pivot row
            print(f"➡️ Scaling row {pivot_row} to make pivot = 1")
            augmented_matrix[pivot_row] = augmented_matrix[pivot_row] / pivot_value
            print(augmented_matrix,"\n")

            # Eliminate Pivot Column from other rows
            for target_row in range(num_rows):
                if target_row != pivot_row:
                    factor = augmented_matrix[target_row, pivot_row]  # value to eliminate
                    augmented_matrix[target_row, :] -= factor * augmented_matrix[pivot_row, :]

        # Extract right half → inverse
        inverse_matrix = augmented_matrix[:, num_rows:]
        print("✅ Inverse matrix A⁻¹:")
        print(inverse_matrix)

        return Matrix(inverse_matrix)


    def return_matrix(self):
        return self.data
    
    def print_matrix(self):
        print(self.data)
        return self